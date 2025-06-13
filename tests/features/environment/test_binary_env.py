from deepdiff import DeepDiff

from SAF.features.environment.binary import compute_features


def test_compute_binary_env_features_ThSb(ThSb_cif):
    actual = compute_features(ThSb_cif)
    expected = {
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
    }
    diff = DeepDiff(actual, expected, significant_digits=3)
    assert diff == {}


def test_compute_binary_env_features_RhSb2(RhSb2_cif):
    actual = compute_features(RhSb2_cif)
    expected = {
        "ENV_A_shortest_dist_count": 1,
        "ENV_B_shortest_dist_count": 1,
        "ENV_A_avg_shortest_dist_count": 1.0,
        "ENV_B_avg_shortest_dist_count": 1.0,
        "ENV_A_shortest_tol_dist_count": 3,
        "ENV_B_shortest_tol_dist_count": 3,
        "ENV_A_avg_shortest_dist_within_tol_count": 3.0,
        "ENV_B_avg_shortest_dist_within_tol_count": 3.0,
        "ENV_A_second_by_first_shortest_dist": 1.0151033386327504,
        "ENV_B_second_by_first_shortest_dist": 1.0151033386327504,
        "ENV_A_avg_second_by_first_shortest_dist": 1.0151033386327504,
        "ENV_B_avg_second_by_first_shortest_dist": 1.0084943540825893,
        "ENV_A_second_shortest_dist_count": 1,
        "ENV_B_second_shortest_dist_count": 1,
        "ENV_A_avg_second_shortest_dist_count": 1.0,
        "ENV_B_avg_second_shortest_dist_count": 1.0,
        "ENV_A_homoatomic_dist_by_shortest_dist": 1.1971383147853736,
        "ENV_B_homoatomic_dist_by_shortest_dist": 1.1244038155802862,
        "ENV_A_avg_homoatomic_dist_by_shortest_dist": 1.1971383147853736,
        "ENV_B_avg_homoatomic_dist_by_shortest_dist": 1.095572948514125,
        "ENV_A_count_at_A_shortest_dist": 0,
        "ENV_A_count_at_B_shortest_dist": 1,
        "ENV_A_avg_count_at_A_shortest_dist": 0.0,
        "ENV_A_avg_count_at_B_shortest_dist": 1.0,
        "ENV_B_count_at_A_shortest_dist": 1,
        "ENV_B_count_at_B_shortest_dist": 0,
        "ENV_B_avg_count_at_A_shortest_dist": 1.0,
        "ENV_B_avg_count_at_B_shortest_dist": 0.0,
    }
    diff = DeepDiff(actual, expected, significant_digits=3)
    assert diff == {}
