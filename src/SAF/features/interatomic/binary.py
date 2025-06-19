from cifkit import Cif
from cifkit.data import radius_optimization as radius_opt

from SAF.features.interatomic import helper
from SAF.utils import bond, packing


def compute_features(cif: Cif, use_size_constraint: bool, elements):
    A, B = elements
    A_CIF_rad = cif.radius_values[A]["CIF_radius"]
    B_CIF_rad = cif.radius_values[B]["CIF_radius"]
    CIF_rad_refined, obj_value = radius_opt.get_refined_CIF_radius(
        [A, B], cif.shortest_bond_pair_distance, elements_ordered=False, use_size_constraint=use_size_constraint
    )
    min_bond_dists = bond.get_min_distances_by_labels(cif.shortest_bond_pair_distance, [A, B], labels=["A", "B"])
    AA_dist = min_bond_dists["AA"]
    BB_dist = min_bond_dists["BB"]
    AB_dist = min_bond_dists["AB"]
    A_CIF_rad_refined = float(CIF_rad_refined[A])
    B_CIF_rad_refined = float(CIF_rad_refined[B])
    # Distances
    AA_dist_by_2 = AA_dist / 2
    BB_dist_by_2 = BB_dist / 2
    # Refined distances
    AA_ref_radius_sum = 2 * A_CIF_rad_refined
    BB_ref_radius_sum = 2 * B_CIF_rad_refined
    AB_ref_radius_sum = A_CIF_rad_refined + B_CIF_rad_refined
    # Percent differences between refined and CIF radii
    percent_diff_A = (A_CIF_rad_refined - A_CIF_rad) / A_CIF_rad
    percent_diff_B = (B_CIF_rad_refined - B_CIF_rad) / B_CIF_rad
    # Interatomic distance features
    Asize_by_Bsize = A_CIF_rad / B_CIF_rad
    AA_dist_by_2_by_Asize = AA_dist_by_2 / A_CIF_rad
    BB_dist_by_2_by_Bsize = BB_dist_by_2 / B_CIF_rad
    AB_dist_by_ABsizes = AB_dist / (A_CIF_rad + B_CIF_rad)
    AA_dist_minus_ref_diff = (AA_dist - AA_ref_radius_sum) / AA_dist
    BB_dist_minus_ref_diff = (BB_dist - BB_ref_radius_sum) / BB_dist
    AB_dist_minus_ref_diff = (AB_dist - AB_ref_radius_sum) / AB_dist
    # UNI Homoatomic and heteroatomic distances
    homoatomic_dists = helper.get_bond_distances_by_labels(min_bond_dists, ["AA", "BB"])
    heteroatomic_dists = helper.get_bond_distances_by_labels(min_bond_dists, ["AB"])
    shortest_heteroatomic_dist = helper.get_min_from_dists(heteroatomic_dists)
    shortest_homoatomic_dist = helper.get_min_from_dists(homoatomic_dists)
    # Define the CIF and refined radii
    rad_dict = {
        "AA": A_CIF_rad,
        "BB": B_CIF_rad,
        "AB": (A_CIF_rad + B_CIF_rad),
    }
    refined_rad_dict = {
        "AA": A_CIF_rad_refined,
        "BB": B_CIF_rad_refined,
        "AB": (A_CIF_rad_refined + B_CIF_rad_refined),
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
    percent_diffs = [percent_diff_A, percent_diff_B]
    highest_refined_percent_diff = helper.get_highest_refined_percent_diff(percent_diffs)
    lowest_refined_percent_diff = helper.get_lowest_refined_percent_diff(percent_diffs)
    # Packing efficiency
    packing_efficiency = packing.compute_efficiency(
        cif,
        {
            A: A_CIF_rad_refined,
            B: B_CIF_rad_refined,
        },
    )
    data = {
        "Entry": cif.file_name_without_ext,
        "Formula": cif.formula,
        "Structure": cif.structure,
        "A": A,
        "B": B,
        "INT_AA_dist": AA_dist,
        "INT_BB_dist": BB_dist,
        "INT_AB_dist": AB_dist,
        "INT_Asize": A_CIF_rad,
        "INT_Bsize": B_CIF_rad,
        "INT_Asize_by_Bsize": Asize_by_Bsize,
        "INT_AA_dist_by_2_by_Asize": AA_dist_by_2_by_Asize,
        "INT_BB_dist_by_2_by_Bsize": BB_dist_by_2_by_Bsize,
        "INT_AB_dist_by_ABsizes": AB_dist_by_ABsizes,
        "INT_Asize_ref": A_CIF_rad_refined,
        "INT_Bsize_ref": B_CIF_rad_refined,
        "INT_percent_diff_A_by_100": percent_diff_A,
        "INT_percent_diff_B_by_100": percent_diff_B,
        "INT_dist_AA_minus_ref_diff": AA_dist_minus_ref_diff,
        "INT_dist_BB_minus_ref_diff": BB_dist_minus_ref_diff,
        "INT_dist_AB_minus_ref_diff": AB_dist_minus_ref_diff,
        "INT_R_factor": obj_value,
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
