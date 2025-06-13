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
    CIF_rad_refined, obj_value = radius_opt.get_refined_CIF_radius(
        [R, M, X], cif.shortest_bond_pair_distance, elements_ordered=False
    )
    R_CIF_rad_refined = CIF_rad_refined[R]
    M_CIF_rad_refined = CIF_rad_refined[M]
    X_CIF_rad_refined = CIF_rad_refined[X]
    # Do not use the alphabetical order of the elements for the refined radius
    min_bond_dists = bond.get_min_distances_by_labels(
        cif.shortest_bond_pair_distance, [R, M, X], labels=["R", "M", "X"]
    )
    distRR = min_bond_dists["RR"]
    distRM = min_bond_dists["RM"]
    distRX = min_bond_dists["RX"]
    distMM = min_bond_dists["MM"]
    distMX = min_bond_dists["MX"]
    distXX = min_bond_dists["XX"]
    # Distances
    distRM_by_R_and_M_sizes_combined = distRM / (R_CIF_rad + M_CIF_rad)
    distRX_by_R_and_X_sizes_combined = distRX / (R_CIF_rad + X_CIF_rad)
    distMX_by_M_and_X_sizes_combined = distMX / (M_CIF_rad + X_CIF_rad)
    distRR_by_2 = distRR / 2
    distMM_by_2 = distMM / 2
    distXX_by_2 = distXX / 2

    RR_radius_sum = 2 * R_CIF_rad_refined
    MM_radius_sum = 2 * M_CIF_rad_refined
    XX_radius_sum = 2 * X_CIF_rad_refined
    RM_radius_sum = R_CIF_rad_refined + M_CIF_rad_refined
    RX_radius_sum = R_CIF_rad_refined + X_CIF_rad_refined
    MX_radius_sum = M_CIF_rad_refined + X_CIF_rad_refined
    # Percent differences between refined and CIF radii
    percent_diff_R = (R_CIF_rad_refined - R_CIF_rad) / R_CIF_rad
    percent_diff_M = (M_CIF_rad_refined - M_CIF_rad) / M_CIF_rad
    percent_diff_X = (X_CIF_rad_refined - X_CIF_rad) / X_CIF_rad
    # Interatomic distance features
    Rsize_by_Msize = R_CIF_rad / M_CIF_rad
    Msize_by_Xsize = M_CIF_rad / X_CIF_rad
    Rsize_by_Xsize = R_CIF_rad / X_CIF_rad

    distRR_by_byRsize = distRR_by_2 / R_CIF_rad
    distMM_by_byMsize = distMM_by_2 / M_CIF_rad
    distXX_by_byXsize = distXX_by_2 / X_CIF_rad
    distRM_by_R_and_M_sizes_combined = distRM / (R_CIF_rad + M_CIF_rad)
    distMX_by_M_and_X_sizes_combined = distMX / (M_CIF_rad + X_CIF_rad)

    RR_minus_ref_diff = (distRR - RR_radius_sum) / distRR
    MM_minus_ref_diff = (distMM - MM_radius_sum) / distMM
    XX_minus_ref_diff = (distXX - XX_radius_sum) / distXX
    RM_minus_ref_diff = (distRM - RM_radius_sum) / distRM
    RX_minus_ref_diff = (distRX - RX_radius_sum) / distRX
    MX_minus_ref_diff = (distMX - MX_radius_sum) / distMX

    # Get the shortest homo/hetroatomic distance
    homoatomic_dists = helper.get_bond_distances_by_labels(min_bond_dists, ["RR", "MM", "XX"])
    heteroatomic_dists = helper.get_bond_distances_by_labels(min_bond_dists, ["RM", "MX", "RX"])
    shortest_heteroatomic_dist = helper.get_min_from_dists(heteroatomic_dists)
    shortest_homoatomic_dist = helper.get_min_from_dists(homoatomic_dists)

    # Parse the CIF radius based on the shortest homo/heteroatomic dist
    rad_dict = {
        "RR": R_CIF_rad,
        "MM": M_CIF_rad,
        "XX": X_CIF_rad,
        "RM": (R_CIF_rad + M_CIF_rad),
        "MX": (M_CIF_rad + X_CIF_rad),
        "RX": (R_CIF_rad + X_CIF_rad),
    }

    refined_rad_dict = {
        "RR": R_CIF_rad_refined,
        "MM": M_CIF_rad_refined,
        "XX": X_CIF_rad_refined,
        "RM": (R_CIF_rad_refined + M_CIF_rad_refined),
        "MX": (M_CIF_rad_refined + X_CIF_rad_refined),
        "RX": (R_CIF_rad_refined + X_CIF_rad_refined),
    }

    percent_diffs = [percent_diff_R, percent_diff_M, percent_diff_X]
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
        "INT_distRR": distRR,
        "INT_distMM": distMM,
        "INT_distXX": distXX,
        "INT_distRM": distRM,
        "INT_distMX": distMX,
        "INT_distRX": distRX,
        "INT_Rsize": R_CIF_rad,
        "INT_Msize": M_CIF_rad,
        "INT_Xsize": X_CIF_rad,
        "INT_Rsize_by_Msize": Rsize_by_Msize,
        "INT_Msize_by_Xsize": Msize_by_Xsize,
        "INT_Rsize_by_Xsize": Rsize_by_Xsize,
        "INT_distRR_by2_byRsize": distRR_by_byRsize,
        "INT_distMM_by2_byMsize": distMM_by_byMsize,
        "INT_distXX_by2_byXsize": distXX_by_byXsize,
        "INT_distRM_byRsizebyMsize": distRM_by_R_and_M_sizes_combined,
        "INT_distMX_byMsizebyXsize": distMX_by_M_and_X_sizes_combined,
        "INT_distRX_byRsizebyXsize": distRX_by_R_and_X_sizes_combined,
        "INT_Rsize_ref": R_CIF_rad_refined,
        "INT_Msize_ref": M_CIF_rad_refined,
        "INT_Xsize_ref": X_CIF_rad_refined,
        "INT_percent_diff_R_by_100": percent_diff_R,
        "INT_percent_diff_M_by_100": percent_diff_M,
        "INT_percent_diff_X_by_100": percent_diff_X,
        "INT_distRR_minus_ref_diff": RR_minus_ref_diff,
        "INT_distMM_minus_ref_diff": MM_minus_ref_diff,
        "INT_distXX_minus_ref_diff": XX_minus_ref_diff,
        "INT_distRM_minus_ref_diff": RM_minus_ref_diff,
        "INT_distMX_minus_ref_diff": MX_minus_ref_diff,
        "INT_distRX_minus_ref_diff": RX_minus_ref_diff,
        "INT_R_factor": obj_value,
        "INT_UNI_shortest_homoatomic_dist": shortest_homoatomic_dist,
        "INT_UNI_shortest_heteroatomic_dist": shortest_heteroatomic_dist,
        "INT_UNI_shortest_homoatomic_dist_by_2_by_atom_size": uni_features[
            "shortest_homoatomic_dist_by_2_by_atom_size"
        ],
        "INT_UNI_shortest_heteroatomic_dist_by_sum_of_atom_sizes": uni_features[
            "shortest_heteroatomic_dist_by_sum_of_atom_sizes"
        ],
        "INT_UNI_shortest_homoatomic_dist_by_2_by_refined_atom_size": uni_features[
            "shortest_homoatomic_dist_by_2_by_refined_atom_sizes"
        ],
        "INT_UNI_shortest_heteroatomic_dist_by_sum_of_refined_atom_sizes": uni_features[
            "shortest_heteroatomic_dist_by_refined_atom_sizes"
        ],
        "INT_UNI_highest_refined_percent_diff_abs": highest_refined_percent_diff,
        "INT_UNI_lowest_refined_percent_diff_abs": lowest_refined_percent_diff,
        "INT_UNI_refined_packing_efficiency": packing_efficiency,
    }

    uni_data = {
        "Entry": cif.file_name_without_ext,
        "Formula": cif.formula,
        "INT_UNI_shortest_homoatomic_dist": shortest_homoatomic_dist,
        "INT_UNI_shortest_heteroatomic_dist": shortest_heteroatomic_dist,
        "INT_UNI_shortest_homoatomic_dist_by_2_by_atom_size": uni_features[
            "shortest_homoatomic_dist_by_2_by_atom_size"
        ],
        "INT_UNI_shortest_heteroatomic_dist_by_sum_of_atom_sizes": uni_features[
            "shortest_heteroatomic_dist_by_sum_of_atom_sizes"
        ],
        "INT_UNI_shortest_homoatomic_dist_by_2_by_refined_atom_size": uni_features[
            "shortest_homoatomic_dist_by_2_by_refined_atom_sizes"
        ],
        "INT_UNI_shortest_heteroatomic_dist_by_sum_of_refined_atom_sizes": uni_features[
            "shortest_heteroatomic_dist_by_refined_atom_sizes"
        ],
        "INT_UNI_highest_refined_percent_diff_abs": highest_refined_percent_diff,
        "INT_UNI_lowest_refined_percent_diff_abs": lowest_refined_percent_diff,
        "INT_UNI_refined_packing_efficiency": packing_efficiency,
    }
    # log.print_dict_pretty(data, "ternar_int")
    return data, uni_data
