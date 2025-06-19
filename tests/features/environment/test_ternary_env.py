from deepdiff import DeepDiff

from SAF.features.environment.ternary import compute_features


def test_compute_binary_env_features_ThSb(URhIn_cif, URhIn_elements_tuple):
    actual = compute_features(URhIn_cif, URhIn_elements_tuple)
    expected = {
        "ENV_R_shortest_dist_count": 3,
        "ENV_M_shortest_dist_count": 6,
        "ENV_X_shortest_dist_count": 2,
        "ENV_R_avg_shortest_dist_count": 3.0,
        "ENV_M_avg_shortest_dist_count": 4.0,
        "ENV_X_avg_shortest_dist_count": 2.0,
        "ENV_R_shortest_tol_dist_count": 5,
        "ENV_M_shortest_tol_dist_count": 6,
        "ENV_X_shortest_tol_dist_count": 2,
        "ENV_R_avg_shortest_dist_within_tol_count": 5.0,
        "ENV_M_avg_shortest_dist_within_tol_count": 7.5,
        "ENV_X_avg_shortest_dist_within_tol_count": 2.0,
        "ENV_R_second_by_first_shortest_dist": 1.000335232986926,
        "ENV_M_second_by_first_shortest_dist": 1.1294030404152762,
        "ENV_X_second_by_first_shortest_dist": 1.057471264367816,
        "ENV_R_avg_second_by_first_shortest_dist": 1.000335232986926,
        "ENV_M_avg_second_by_first_shortest_dist": 1.0648768357756606,
        "ENV_X_avg_second_by_first_shortest_dist": 1.057471264367816,
        "ENV_R_second_shortest_dist_count": 1,
        "ENV_M_second_shortest_dist_count": 3,
        "ENV_X_second_shortest_dist_count": 2,
        "ENV_R_avg_second_shortest_dist_count": 1.0,
        "ENV_M_avg_second_shortest_dist_count": 2.0,
        "ENV_X_avg_second_shortest_dist_count": 2.0,
        "ENV_R_homoatomic_dist_by_shortest_dist": 1.3010392222594702,
        "ENV_M_homoatomic_dist_by_shortest_dist": 1.4390063032999627,
        "ENV_X_homoatomic_dist_by_shortest_dist": 1.2028179458657768,
        "ENV_R_avg_homoatomic_dist_by_shortest_dist": 1.3010392222594702,
        "ENV_M_avg_homoatomic_dist_by_shortest_dist": 1.3999028711450725,
        "ENV_X_avg_homoatomic_dist_by_shortest_dist": 1.2028179458657768,
        "ENV_R_count_at_R_shortest_dist": 0,
        "ENV_M_count_at_R_shortest_dist": 3,
        "ENV_X_count_at_R_shortest_dist": 0,
        "ENV_R_avg_count_at_R_shortest_dist": 0.0,
        "ENV_M_avg_count_at_R_shortest_dist": 0.0,
        "ENV_X_avg_count_at_R_shortest_dist": 0.0,
        "ENV_R_count_at_M_shortest_dist": 0,
        "ENV_M_count_at_M_shortest_dist": 0,
        "ENV_X_count_at_M_shortest_dist": 6,
        "ENV_R_avg_count_at_M_shortest_dist": 1.5,
        "ENV_M_avg_count_at_M_shortest_dist": 0.0,
        "ENV_X_avg_count_at_M_shortest_dist": 1.0,
        "ENV_R_count_at_X_shortest_dist": 0,
        "ENV_M_count_at_X_shortest_dist": 2,
        "ENV_X_count_at_X_shortest_dist": 0,
        "ENV_R_avg_count_at_X_shortest_dist": 0.0,
        "ENV_M_avg_count_at_X_shortest_dist": 8.0,
        "ENV_X_avg_count_at_X_shortest_dist": 0.0,
    }
    diff = DeepDiff(actual, expected, significant_digits=3)
    assert diff == {}
