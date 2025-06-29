from deepdiff import DeepDiff

from SAF.features.generator import compute_binary_features


def test_generate_binary_features():
    file_path = "tests/cif/binary/ThSb.cif"
    actual_features, actual_uni_features = compute_binary_features(file_path)
    expected_features = {
        "Entry": "ThSb",
        "Formula": "ThSb",
        "Structure": "CsCl",
        "A": "Th",
        "B": "Sb",
        "INT_AA_dist": 3.847,
        "INT_BB_dist": 3.847,
        "INT_AB_dist": 3.332,
        "INT_Asize": 1.798,
        "INT_Bsize": 1.434,
        "INT_Asize_by_Bsize": 1.2538354253835426,
        "INT_AA_dist_by_2_by_Asize": 1.0697997775305894,
        "INT_BB_dist_by_2_by_Bsize": 1.341352859135286,
        "INT_AB_dist_by_ABsizes": 1.0309405940594059,
        "INT_Asize_ref": 1.8591213139280958,
        "INT_Bsize_ref": 1.4728786860719039,
        "INT_percent_diff_A_by_100": 0.03399405668970841,
        "INT_percent_diff_B_by_100": 0.027112054443447647,
        "INT_dist_AA_minus_ref_diff": 0.033469553455629956,
        "INT_dist_BB_minus_ref_diff": 0.2342715435030393,
        "INT_dist_AB_minus_ref_diff": 0.0,
        "INT_R_factor": 0.0018906593863675784,
        "INT_UNI_shortest_homoatomic_dist": 3.847,
        "INT_UNI_shortest_heteroatomic_dist": 3.332,
        "INT_UNI_shortest_homoatomic_dist_by_2_by_atom_size": 1.0697997775305894,
        "INT_UNI_shortest_heteroatomic_dist_by_sum_of_atom_sizes": 1.0309405940594059,
        "INT_UNI_shortest_homoatomic_dist_by_2_by_refined_atom_size": 1.0346285557535135,
        "INT_UNI_shortest_heteroatomic_dist_by_sum_of_refined_atom_sizes": 1.0,
        "INT_UNI_highest_refined_percent_diff_abs": 0.03399405668970841,
        "INT_UNI_lowest_refined_percent_diff_abs": 0.027112054443447647,
        "INT_UNI_refined_packing_efficiency": 0.7078488680834484,
        "WYK_A_lowest_wyckoff": 1,
        "WYK_B_lowest_wyckoff": 1,
        "WYK_identical_lowest_wyckoff_count": 2,
        "WYK_A_sites_total": 1,
        "WYK_B_sites_total": 1,
        "WYK_A_multiplicity_total": 1,
        "WYK_B_multiplicity_total": 1,
        "ENV_A_shortest_dist_count": 8,
        "ENV_B_shortest_dist_count": 8,
        "ENV_A_avg_shortest_dist_count": 8.0,
        "ENV_B_avg_shortest_dist_count": 8.0,
        "ENV_A_shortest_tol_dist_count": 8,
        "ENV_B_shortest_tol_dist_count": 8,
        "ENV_A_avg_shortest_dist_within_tol_count": 8.0,
        "ENV_B_avg_shortest_dist_within_tol_count": 8.0,
        "ENV_A_second_by_first_shortest_dist": 1.154561824729892,
        "ENV_B_second_by_first_shortest_dist": 1.154561824729892,
        "ENV_A_avg_second_by_first_shortest_dist": 1.154561824729892,
        "ENV_B_avg_second_by_first_shortest_dist": 1.154561824729892,
        "ENV_A_second_shortest_dist_count": 6,
        "ENV_B_second_shortest_dist_count": 6,
        "ENV_A_avg_second_shortest_dist_count": 6.0,
        "ENV_B_avg_second_shortest_dist_count": 6.0,
        "ENV_A_homoatomic_dist_by_shortest_dist": 1.154561824729892,
        "ENV_B_homoatomic_dist_by_shortest_dist": 1.154561824729892,
        "ENV_A_avg_homoatomic_dist_by_shortest_dist": 1.154561824729892,
        "ENV_B_avg_homoatomic_dist_by_shortest_dist": 1.154561824729892,
        "ENV_A_count_at_A_shortest_dist": 0,
        "ENV_A_count_at_B_shortest_dist": 8,
        "ENV_A_avg_count_at_A_shortest_dist": 0.0,
        "ENV_A_avg_count_at_B_shortest_dist": 8.0,
        "ENV_B_count_at_A_shortest_dist": 8,
        "ENV_B_count_at_B_shortest_dist": 0,
        "ENV_B_avg_count_at_A_shortest_dist": 8.0,
        "ENV_B_avg_count_at_B_shortest_dist": 0.0,
        "CN_AVG_coordination_number": 14.0,
        "CN_AVG_A_atom_count": 7.0,
        "CN_AVG_B_atom_count": 7.0,
        "CN_AVG_polyhedron_volume": 113.86449999999999,
        "CN_AVG_central_atom_to_center_of_mass_dist": 0.0005,
        "CN_AVG_number_of_edges": 36.0,
        "CN_AVG_number_of_faces": 24.0,
        "CN_AVG_shortest_distance_to_face": 2.7945,
        "CN_AVG_shortest_distance_to_edge": 2.72,
        "CN_AVG_volume_of_inscribed_sphere": 91.398,
        "CN_AVG_packing_efficiency": 0.803,
        "CN_MIN_coordination_number": 14.0,
        "CN_MIN_A_atom_count": 7.0,
        "CN_MIN_B_atom_count": 7.0,
        "CN_MIN_polyhedron_volume": 113.86449999999999,
        "CN_MIN_central_atom_to_center_of_mass_dist": 0.0005,
        "CN_MIN_number_of_edges": 36.0,
        "CN_MIN_number_of_faces": 24.0,
        "CN_MIN_shortest_distance_to_face": 2.7945,
        "CN_MIN_shortest_distance_to_edge": 2.72,
        "CN_MIN_volume_of_inscribed_sphere": 91.398,
        "CN_MIN_packing_efficiency": 0.803,
        "CN_MAX_coordination_number": 14.0,
        "CN_MAX_A_atom_count": 7.0,
        "CN_MAX_B_atom_count": 7.0,
        "CN_MAX_polyhedron_volume": 113.86449999999999,
        "CN_MAX_central_atom_to_center_of_mass_dist": 0.0005,
        "CN_MAX_number_of_edges": 36.0,
        "CN_MAX_number_of_faces": 24.0,
        "CN_MAX_shortest_distance_to_face": 2.7945,
        "CN_MAX_shortest_distance_to_edge": 2.72,
        "CN_MAX_volume_of_inscribed_sphere": 91.398,
        "CN_MAX_packing_efficiency": 0.803,
    }
    # THis works but just unstable.
    diff = DeepDiff(expected_features, actual_features, significant_digits=3)
    assert diff == {}
    expected_uni_features = {
        "Entry": "ThSb",
        "Formula": "ThSb",
        "INT_UNI_shortest_homoatomic_dist": 3.847,
        "INT_UNI_shortest_heteroatomic_dist": 3.332,
        "INT_UNI_shortest_homoatomic_dist_by_2_by_atom_size": 1.0697997775305894,
        "INT_UNI_shortest_heteroatomic_dist_by_sum_of_atom_sizes": 1.0309405940594059,
        "INT_UNI_shortest_homoatomic_dist_by_2_by_refined_atom_size": 1.0346285557535135,
        "INT_UNI_shortest_heteroatomic_dist_by_sum_of_refined_atom_sizes": 1.0,
        "INT_UNI_highest_refined_percent_diff_abs": 0.03399405668970841,
        "INT_UNI_lowest_refined_percent_diff_abs": 0.027112054443447647,
        "INT_UNI_refined_packing_efficiency": 0.7078488680834484,
        "UNI_WYK_lowest_wyckoff": 1,
    }
    diff = DeepDiff(expected_uni_features, actual_uni_features, significant_digits=3)
    assert diff == {}
