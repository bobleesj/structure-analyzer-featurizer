from cifkit import Cif
from cifkit.data import radius_optimization as radius_opt

from SAF.features.interatomic import helper
from SAF.utils import bond, element_order, packing


def compute_features(cif: Cif):
    elements = list(cif.unique_elements)
    R, M, X = element_order.get_ternary_RMX_elements(elements)
    R_CIF_rad = cif.radius_values[R]["CIF_radius"]
    M_CIF_rad = cif.radius_values[M]["CIF_radius"]
    X_CIF_rad = cif.radius_values[X]["CIF_radius"]
    CIF_rad_refined, obj_value = radius_opt.get_refined_CIF_radius([R, M, X], cif.shortest_bond_pair_distance, elements_ordered=False)
    R_CIF_rad_refined = float(CIF_rad_refined[R])
    M_CIF_rad_refined = float(CIF_rad_refined[M])
    X_CIF_rad_refined = float(CIF_rad_refined[X])
    # Do not use the alphabetical order of the elements for the refined radius
    min_bond_dists = bond.get_min_distances_by_labels(cif.shortest_bond_pair_distance, [R, M, X], labels=["R", "M", "X"])
    # 1) Min bond distances
    RR_dist = min_bond_dists["RR"]
    RM_dist = min_bond_dists["RM"]
    RX_dist = min_bond_dists["RX"]
    MM_dist = min_bond_dists["MM"]
    MX_dist = min_bond_dists["MX"]
    XX_dist = min_bond_dists["XX"]
    # 2) Radius from interatomic distances divided by CIF radius
    RM_dist_by_RM_sizes = RM_dist / (R_CIF_rad + M_CIF_rad)
    RX_dist_by_RX_sizes = RX_dist / (R_CIF_rad + X_CIF_rad)
    MX_dist_by_MX_sizes = MX_dist / (M_CIF_rad + X_CIF_rad)
    # 3) Radius from interatomic distances divided by 2 (3 of them for ternary)
    RR_dist_by_2 = RR_dist / 2
    MM_dist_by_2 = MM_dist / 2
    XX_dist_by_2 = XX_dist / 2
    # 4) Refined radius sums (6 of them for ternary)
    RR_ref_rad_sum = 2 * R_CIF_rad_refined
    MM_ref_rad_sum = 2 * M_CIF_rad_refined
    XX_ref_rad_sum = 2 * X_CIF_rad_refined
    RM_ref_rad_sum = R_CIF_rad_refined + M_CIF_rad_refined
    RX_ref_rad_sum = R_CIF_rad_refined + X_CIF_rad_refined
    MX_ref_rad_sum = M_CIF_rad_refined + X_CIF_rad_refined
    # 5) Percent differences between refined and CIF radius
    percent_diff_R = (R_CIF_rad_refined - R_CIF_rad) / R_CIF_rad
    percent_diff_M = (M_CIF_rad_refined - M_CIF_rad) / M_CIF_rad
    percent_diff_X = (X_CIF_rad_refined - X_CIF_rad) / X_CIF_rad
    # 6) Size ratios of CIF radius
    Rsize_by_Msize = R_CIF_rad / M_CIF_rad
    Msize_by_Xsize = M_CIF_rad / X_CIF_rad
    Rsize_by_Xsize = R_CIF_rad / X_CIF_rad
    # 7) Radius from interatomic distances divided by CIF radius
    RR_dist_by_2_by_Rsize = RR_dist_by_2 / R_CIF_rad
    MM_dist_by_2_by_Msize = MM_dist_by_2 / M_CIF_rad
    XX_dist_by_2_by_Xsize = XX_dist_by_2 / X_CIF_rad
    # 8) Difference between the iteratomic distance and the expected refined radius sum
    RR_minus_ref_diff = (RR_dist - RR_ref_rad_sum) / RR_dist
    MM_minus_ref_diff = (MM_dist - MM_ref_rad_sum) / MM_dist
    XX_minus_ref_diff = (XX_dist - XX_ref_rad_sum) / XX_dist
    RM_minus_ref_diff = (RM_dist - RM_ref_rad_sum) / RM_dist
    RX_minus_ref_diff = (RX_dist - RX_ref_rad_sum) / RX_dist
    MX_minus_ref_diff = (MX_dist - MX_ref_rad_sum) / MX_dist
    # 9) Get the shortest homo/hetroatomic distance
    homoatomic_dists = helper.get_bond_distances_by_labels(min_bond_dists, ["RR", "MM", "XX"])
    heteroatomic_dists = helper.get_bond_distances_by_labels(min_bond_dists, ["RM", "MX", "RX"])
    shortest_heteroatomic_dist = helper.get_min_from_dists(heteroatomic_dists)
    shortest_homoatomic_dist = helper.get_min_from_dists(homoatomic_dists)
    # Parse the CIF radius based on the shortest homo/heteroatomic dist
    rad_dict = {
        "RR": R_CIF_rad,
        "MM": M_CIF_rad,
        "XX": X_CIF_rad,
        "RM": R_CIF_rad + M_CIF_rad,
        "MX": M_CIF_rad + X_CIF_rad,
        "RX": R_CIF_rad + X_CIF_rad,
    }

    refined_rad_dict = {
        "RR": R_CIF_rad_refined,
        "MM": M_CIF_rad_refined,
        "XX": X_CIF_rad_refined,
        "RM": R_CIF_rad_refined + M_CIF_rad_refined,
        "MX": M_CIF_rad_refined + X_CIF_rad_refined,
        "RX": R_CIF_rad_refined + X_CIF_rad_refined,
    }
    shortest_homo_key = helper.get_shortest_homo_key(min_bond_dists, shortest_homoatomic_dist)
    shortest_hetero_key = helper.get_shortest_hetero_key(min_bond_dists, shortest_heteroatomic_dist)
    uni_features = helper.get_shortest_homo_heteroatomic_features(
        shortest_homoatomic_dist,
        shortest_homo_key,
        shortest_heteroatomic_dist,
        shortest_hetero_key,
        rad_dict,
        refined_rad_dict,
    )
    percent_diffs = [percent_diff_R, percent_diff_M, percent_diff_X]
    highest_refined_percent_diff = helper.get_highest_refined_percent_diff(percent_diffs)
    lowest_refined_percent_diff = helper.get_lowest_refined_percent_diff(percent_diffs)
    # Packing efficiency
    packing_efficiency = packing.compute_efficiency(
        cif,
        {
            R: R_CIF_rad_refined,
            M: M_CIF_rad_refined,
            X: X_CIF_rad_refined,
        },
    )
    data = {
        "Entry": cif.file_name_without_ext,
        "Formula": cif.formula,
        "Structure": cif.structure,
        "R": R,
        "M": M,
        "X": X,
        # 1. Shortest distances
        "INT_RR_dist": RR_dist,
        "INT_MM_dist": MM_dist,
        "INT_XX_dist": XX_dist,
        "INT_RM_dist": RM_dist,
        "INT_MX_dist": MX_dist,
        "INT_RX_dist": RX_dist,
        # 2. CIF radius
        "INT_Rsize": R_CIF_rad,
        "INT_Msize": M_CIF_rad,
        "INT_Xsize": X_CIF_rad,
        # 3. CIF radius ratio
        "INT_Rsize_by_Msize": Rsize_by_Msize,
        "INT_Msize_by_Xsize": Msize_by_Xsize,
        "INT_Rsize_by_Xsize": Rsize_by_Xsize,
        # 4. Radius from distance divided by CIF radius
        "INT_RR_dist_by_2_by_Rsize": RR_dist_by_2_by_Rsize,
        "INT_MM_dist_by_2_by_Msize": MM_dist_by_2_by_Msize,
        "INT_XX_dist_by_2_by_Xsize": XX_dist_by_2_by_Xsize,
        "INT_RM_dist_by_RMsizes": RM_dist_by_RM_sizes,
        "INT_MX_dist_by_MXsizes": MX_dist_by_MX_sizes,
        "INT_RX_dist_by_RXsizes": RX_dist_by_RX_sizes,
        # 5. Refined CIF radius
        "INT_Rsize_ref": R_CIF_rad_refined,
        "INT_Msize_ref": M_CIF_rad_refined,
        "INT_Xsize_ref": X_CIF_rad_refined,
        # 6. Difference between CIF radius and refined CIF radius
        "INT_percent_diff_R_by_100": percent_diff_R,
        "INT_percent_diff_M_by_100": percent_diff_M,
        "INT_percent_diff_X_by_100": percent_diff_X,
        # 7. Difference between interatomic distance and refined radius sum
        "INT_RR_dist_minus_ref_diff": RR_minus_ref_diff,
        "INT_MM_dist_minus_ref_diff": MM_minus_ref_diff,
        "INT_XX_dist_minus_ref_diff": XX_minus_ref_diff,
        "INT_RM_dist_minus_ref_diff": RM_minus_ref_diff,
        "INT_MX_dist_minus_ref_diff": MX_minus_ref_diff,
        "INT_RX_dist_minus_ref_diff": RX_minus_ref_diff,
        # 8. Objective value of the radius optimization
        "INT_R_factor": obj_value,
        # 9. Universal features
        "INT_UNI_shortest_homoatomic_dist": shortest_homoatomic_dist,
        "INT_UNI_shortest_heteroatomic_dist": shortest_heteroatomic_dist,
        "INT_UNI_shortest_homoatomic_dist_by_2_by_atom_size": uni_features["shortest_homoatomic_dist_by_2_by_atom_size"],
        "INT_UNI_shortest_heteroatomic_dist_by_sum_of_atom_sizes": uni_features["shortest_heteroatomic_dist_by_sum_of_atom_sizes"],
        "INT_UNI_shortest_homoatomic_dist_by_2_by_refined_atom_size": uni_features["shortest_homoatomic_dist_by_2_by_refined_atom_sizes"],
        "INT_UNI_shortest_heteroatomic_dist_by_sum_of_refined_atom_sizes": uni_features["shortest_heteroatomic_dist_by_refined_atom_sizes"],
        "INT_UNI_highest_refined_percent_diff_abs": highest_refined_percent_diff,
        "INT_UNI_lowest_refined_percent_diff_abs": lowest_refined_percent_diff,
        "INT_UNI_refined_packing_efficiency": packing_efficiency,
    }
    uni_data = {
        "Entry": cif.file_name_without_ext,
        "Formula": cif.formula,
        "INT_UNI_shortest_homoatomic_dist": shortest_homoatomic_dist,
        "INT_UNI_shortest_heteroatomic_dist": shortest_heteroatomic_dist,
        "INT_UNI_shortest_homoatomic_dist_by_2_by_atom_size": uni_features["shortest_homoatomic_dist_by_2_by_atom_size"],
        "INT_UNI_shortest_heteroatomic_dist_by_sum_of_atom_sizes": uni_features["shortest_heteroatomic_dist_by_sum_of_atom_sizes"],
        "INT_UNI_shortest_homoatomic_dist_by_2_by_refined_atom_size": uni_features["shortest_homoatomic_dist_by_2_by_refined_atom_sizes"],
        "INT_UNI_shortest_heteroatomic_dist_by_sum_of_refined_atom_sizes": uni_features["shortest_heteroatomic_dist_by_refined_atom_sizes"],
        "INT_UNI_highest_refined_percent_diff_abs": highest_refined_percent_diff,
        "INT_UNI_lowest_refined_percent_diff_abs": lowest_refined_percent_diff,
        "INT_UNI_refined_packing_efficiency": packing_efficiency,
    }
    return data, uni_data
