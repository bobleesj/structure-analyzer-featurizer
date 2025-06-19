import pytest

from SAF.features.interatomic.ternary import compute_features


def test_compute_ternary_interatomic_feature(URhIn_cif, URhIn_elements_tuple):
    actual, _ = compute_features(URhIn_cif, True, URhIn_elements_tuple)
    expected = {
        "Entry": "URhIn",
        "Formula": "URhIn",
        "Structure": "ZrNiAl",
        "R": "U",
        "M": "Rh",
        "X": "In",
        "INT_RR_dist": 3.881,
        "INT_MM_dist": 3.881,
        "INT_XX_dist": 3.244,
        "INT_RM_dist": 2.983,
        "INT_MX_dist": 2.697,
        "INT_RX_dist": 3.21,
        "INT_Rsize": 1.377,
        "INT_Msize": 1.345,
        "INT_Xsize": 1.624,
        "INT_Rsize_by_Msize": 1.0237918215613384,
        "INT_Msize_by_Xsize": 0.8282019704433496,
        "INT_Rsize_by_Xsize": 0.8479064039408867,
        "INT_RR_dist_by_2_by_Rsize": 1.4092229484386347,
        "INT_MM_dist_by_2_by_Msize": 1.4427509293680296,
        "INT_XX_dist_by_2_by_Xsize": 0.9987684729064039,
        "INT_RM_dist_by_RMsizes": 1.0958853783982367,
        "INT_MX_dist_by_MXsizes": 0.9083866621758167,
        "INT_RX_dist_by_RXsizes": 1.0696434521826057,
        "INT_Rsize_ref": 1.4874430151209064,
        "INT_Msize_ref": 1.3560056919905379,
        "INT_Xsize_ref": 1.4864270730120939,
        "INT_percent_diff_R_by_100": 0.08020553022578532,
        "INT_percent_diff_M_by_100": 0.008182670624935252,
        "INT_percent_diff_X_by_100": -0.0847123934654595,
        "INT_RR_dist_minus_ref_diff": 0.2334743544854901,
        "INT_MM_dist_minus_ref_diff": 0.3012080948257985,
        "INT_XX_dist_minus_ref_diff": 0.08358380208872147,
        "INT_RM_dist_minus_ref_diff": 0.04678219674440349,
        "INT_MX_dist_minus_ref_diff": -0.05392390248521745,
        "INT_RX_dist_minus_ref_diff": 0.07356072020778807,
        "INT_R_factor": 0.013676072784002367,
        "INT_UNI_shortest_homoatomic_dist": 3.244,
        "INT_UNI_shortest_heteroatomic_dist": 2.697,
        "INT_UNI_shortest_homoatomic_dist_by_2_by_atom_size": 0.9987684729064039,
        "INT_UNI_shortest_heteroatomic_dist_by_sum_of_atom_sizes": 0.9083866621758167,
        "INT_UNI_shortest_homoatomic_dist_by_2_by_refined_atom_size": 1.09120725089673,
        "INT_UNI_shortest_heteroatomic_dist_by_sum_of_refined_atom_sizes": 0.948835108153386,
        "INT_UNI_highest_refined_percent_diff_abs": 0.0847123934654595,
        "INT_UNI_lowest_refined_percent_diff_abs": 0.008182670624935252,
        "INT_UNI_refined_packing_efficiency": 0.60664,
    }
    for key, expected_value in expected.items():
        if isinstance(expected_value, float):
            assert actual[key] == pytest.approx(expected_value, abs=0.001)
        else:
            assert actual[key] == expected_value
