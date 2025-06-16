from cifkit import Cif
from cifkit.data import radius_optimization as radius_opt

from SAF.features.interatomic import helper
from SAF.utils import bond, element_order, packing


def compute_features(cif: Cif, use_size_constraint: bool):
    elements = list(cif.unique_elements)
    A, B, C, D = element_order.get_quaternary_ABCD_elements(elements)
    A_CIF_rad = cif.radius_values[A]["CIF_radius"]
    B_CIF_rad = cif.radius_values[B]["CIF_radius"]
    C_CIF_rad = cif.radius_values[C]["CIF_radius"]
    D_CIF_rad = cif.radius_values[D]["CIF_radius"]
    CIF_rad_refined, obj_value = radius_opt.get_refined_CIF_radius(
        [A, B, C, D], cif.shortest_bond_pair_distance, elements_ordered=False, use_size_constraint=use_size_constraint
    )
    A_CIF_rad_refined = float(CIF_rad_refined[A])
    B_CIF_rad_refined = float(CIF_rad_refined[B])
    C_CIF_rad_refined = float(CIF_rad_refined[C])
    D_CIF_rad_refined = float(CIF_rad_refined[D])
    min_bond_dists = bond.get_min_distances_by_labels(cif.shortest_bond_pair_distance, [A, B, C, D], labels=["A", "B", "C", "D"])
    # 1) Min bond distances
    AA_dist = min_bond_dists["AA"]
    AB_dist = min_bond_dists["AB"]
    AC_dist = min_bond_dists["AC"]
    AD_dist = min_bond_dists["AD"]
    BB_dist = min_bond_dists["BB"]
    BC_dist = min_bond_dists["BC"]
    BD_dist = min_bond_dists["BD"]
    CC_dist = min_bond_dists["CC"]
    CD_dist = min_bond_dists["CD"]
    DD_dist = min_bond_dists["DD"]
    # 2) Radius from interatomic distances divided by CIF radius (6 of them for quaternary)
    AB_dist_by_AB_sizes = AB_dist / (A_CIF_rad + B_CIF_rad)
    AC_dist_by_AC_sizes = AC_dist / (A_CIF_rad + C_CIF_rad)
    AD_dist_by_AD_sizes = AD_dist / (A_CIF_rad + D_CIF_rad)
    BC_dist_by_BC_sizes = BC_dist / (B_CIF_rad + C_CIF_rad)
    BD_dist_by_BD_sizes = BD_dist / (B_CIF_rad + D_CIF_rad)
    CD_dist_by_CD_sizes = CD_dist / (C_CIF_rad + D_CIF_rad)
    # 3) Radius from interatomic distances divided by 2
    AA_dist_by_2 = AA_dist / 2
    BB_dist_by_2 = BB_dist / 2
    CC_dist_by_2 = CC_dist / 2
    DD_dist_by_2 = DD_dist / 2
    # 4) Refined radius sums (10 of them for quaternary)
    AA_ref_rad_sum = 2 * A_CIF_rad_refined
    BB_ref_rad_sum = 2 * B_CIF_rad_refined
    CC_ref_rad_sum = 2 * C_CIF_rad_refined
    DD_ref_rad_sum = 2 * D_CIF_rad_refined
    AB_ref_rad_sum = A_CIF_rad_refined + B_CIF_rad_refined
    AC_ref_rad_sum = A_CIF_rad_refined + C_CIF_rad_refined
    AD_ref_rad_sum = A_CIF_rad_refined + D_CIF_rad_refined
    BC_ref_rad_sum = B_CIF_rad_refined + C_CIF_rad_refined
    BD_ref_rad_sum = B_CIF_rad_refined + D_CIF_rad_refined
    CD_ref_rad_sum = C_CIF_rad_refined + D_CIF_rad_refined
    # 5) Percent differences between refined and CIF radii
    percent_diff_A = (A_CIF_rad_refined - A_CIF_rad) / A_CIF_rad
    percent_diff_B = (B_CIF_rad_refined - B_CIF_rad) / B_CIF_rad
    percent_diff_C = (C_CIF_rad_refined - C_CIF_rad) / C_CIF_rad
    percent_diff_D = (D_CIF_rad_refined - D_CIF_rad) / D_CIF_rad
    # 6) Size ratios of CIF radii
    Asize_by_Bsize = A_CIF_rad / B_CIF_rad
    Bsize_by_Csize = B_CIF_rad / C_CIF_rad
    Csize_by_Dsize = C_CIF_rad / D_CIF_rad
    Asize_by_Csize = A_CIF_rad / C_CIF_rad
    Asize_by_Dsize = A_CIF_rad / D_CIF_rad
    Bsize_by_Dsize = B_CIF_rad / D_CIF_rad
    # 7) Radius from interatomic distances divided by CIF radius
    AA_dist_by_2_by_Asize = AA_dist_by_2 / A_CIF_rad
    BB_dist_by_2_by_Bsize = BB_dist_by_2 / B_CIF_rad
    CC_dist_by_2_by_Csize = CC_dist_by_2 / C_CIF_rad
    DD_dist_by_2_by_Dsize = DD_dist_by_2 / D_CIF_rad
    # 8) Difference between the iteratomic distance and the expected refined radius sum
    AA_minus_ref_diff = (AA_dist - AA_ref_rad_sum) / AA_dist
    BB_minus_ref_diff = (BB_dist - BB_ref_rad_sum) / BB_dist
    CC_minus_ref_diff = (CC_dist - CC_ref_rad_sum) / CC_dist
    DD_minus_ref_diff = (DD_dist - DD_ref_rad_sum) / DD_dist
    AB_minus_ref_diff = (AB_dist - AB_ref_rad_sum) / AB_dist
    AC_minus_ref_diff = (AC_dist - AC_ref_rad_sum) / AC_dist
    AD_minus_ref_diff = (AD_dist - AD_ref_rad_sum) / AD_dist
    BC_minus_ref_diff = (BC_dist - BC_ref_rad_sum) / BC_dist
    BD_minus_ref_diff = (BD_dist - BD_ref_rad_sum) / BD_dist
    CD_minus_ref_diff = (CD_dist - CD_ref_rad_sum) / CD_dist
    # 9) Get the shortest homo/hetroatomic distance
    homoatomic_dists = helper.get_bond_distances_by_labels(min_bond_dists, ["AA", "BB", "CC", "DD"])
    heteroatomic_dists = helper.get_bond_distances_by_labels(min_bond_dists, ["AB", "AC", "AD", "BC", "BD", "CD"])
    shortest_heteroatomic_dist = helper.get_min_from_dists(heteroatomic_dists)
    shortest_homoatomic_dist = helper.get_min_from_dists(homoatomic_dists)
    # Parse the CIF radius based on the shortest homo/heteroatomic dist
    rad_dict = {
        "AA": A_CIF_rad,
        "BB": B_CIF_rad,
        "CC": C_CIF_rad,
        "DD": D_CIF_rad,
        "AB": A_CIF_rad + B_CIF_rad,
        "AC": A_CIF_rad + C_CIF_rad,
        "AD": A_CIF_rad + D_CIF_rad,
        "BC": B_CIF_rad + C_CIF_rad,
        "BD": B_CIF_rad + D_CIF_rad,
        "CD": C_CIF_rad + D_CIF_rad,
    }

    refined_rad_dict = {
        "AA": A_CIF_rad_refined,
        "BB": B_CIF_rad_refined,
        "CC": C_CIF_rad_refined,
        "DD": D_CIF_rad_refined,
        "AB": A_CIF_rad_refined + B_CIF_rad_refined,
        "AC": A_CIF_rad_refined + C_CIF_rad_refined,
        "AD": A_CIF_rad_refined + D_CIF_rad_refined,
        "BC": B_CIF_rad_refined + C_CIF_rad_refined,
        "BD": B_CIF_rad_refined + D_CIF_rad_refined,
        "CD": C_CIF_rad_refined + D_CIF_rad_refined,
    }

    percent_diffs = [percent_diff_A, percent_diff_B, percent_diff_C, percent_diff_D]
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
            A: A_CIF_rad_refined,
            B: B_CIF_rad_refined,
            C: C_CIF_rad_refined,
            D: D_CIF_rad_refined,
        },
    )

    # Distances
    data = {
        "Entry": cif.file_name_without_ext,
        "Formula": cif.formula,
        "Structure": cif.structure,
        "A": A,
        "B": B,
        "C": C,
        "D": D,
        # 1. Shortest distances
        "INT_AA_dist": AA_dist,
        "INT_BB_dist": BB_dist,
        "INT_CC_dist": CC_dist,
        "INT_DD_dist": DD_dist,
        "INT_AB_dist": AB_dist,
        "INT_AC_dist": AC_dist,
        "INT_AD_dist": AD_dist,
        "INT_BC_dist": BC_dist,
        "INT_BD_dist": BD_dist,
        "INT_CD_dist": CD_dist,
        # 2. CIF radius
        "INT_Asize": A_CIF_rad,
        "INT_Bsize": B_CIF_rad,
        "INT_Csize": C_CIF_rad,
        "INT_Dsize": D_CIF_rad,
        # 3. CIF radius ratio
        "INT_Asize_by_Bsize": Asize_by_Bsize,
        "INT_Bsize_by_Csize": Bsize_by_Csize,
        "INT_Csize_by_Dsize": Csize_by_Dsize,
        "INT_Asize_by_Csize": Asize_by_Csize,
        "INT_Asize_by_Dsize": Asize_by_Dsize,
        "INT_Bsize_by_Dsize": Bsize_by_Dsize,
        # 4. Radius from distance divided by CIF radius
        "INT_AA_dist_by_2_by_Asize": AA_dist_by_2_by_Asize,
        "INT_BB_dist_by_2_by_Bsize": BB_dist_by_2_by_Bsize,
        "INT_CC_dist_by_2_by_Csize": CC_dist_by_2_by_Csize,
        "INT_DD_dist_by_2_by_Dsize": DD_dist_by_2_by_Dsize,
        "INT_AB_dist_by_ABsizes": AB_dist_by_AB_sizes,
        "INT_AC_dist_by_ACsizes": AC_dist_by_AC_sizes,
        "INT_AD_dist_by_ADsizes": AD_dist_by_AD_sizes,
        "INT_BC_dist_by_BCsizes": BC_dist_by_BC_sizes,
        "INT_BD_dist_by_BDsizes": BD_dist_by_BD_sizes,
        "INT_CD_dist_by_CDsizes": CD_dist_by_CD_sizes,
        # 5. Refined CIF radius
        "INT_Asize_ref": A_CIF_rad_refined,
        "INT_Bsize_ref": B_CIF_rad_refined,
        "INT_Csize_ref": C_CIF_rad_refined,
        "INT_Dsize_ref": D_CIF_rad_refined,
        # 6. Difference between CIF radius and refined CIF radius
        "INT_percent_diff_A_by_100": percent_diff_A,
        "INT_percent_diff_B_by_100": percent_diff_B,
        "INT_percent_diff_C_by_100": percent_diff_C,
        "INT_percent_diff_D_by_100": percent_diff_D,
        # 7. Difference between interatomic an_distce and refined radius sum
        "INT_AA_minus_ref_diff": AA_minus_ref_diff,
        "INT_BB_minus_ref_diff": BB_minus_ref_diff,
        "INT_CC_minus_ref_diff": CC_minus_ref_diff,
        "INT_DD_minus_ref_diff": DD_minus_ref_diff,
        "INT_AB_minus_ref_diff": AB_minus_ref_diff,
        "INT_AC_minus_ref_diff": AC_minus_ref_diff,
        "INT_AD_minus_ref_diff": AD_minus_ref_diff,
        "INT_BC_minus_ref_diff": BC_minus_ref_diff,
        "INT_BD_minus_ref_diff": BD_minus_ref_diff,
        "INT_CD_minus_ref_diff": CD_minus_ref_diff,
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
