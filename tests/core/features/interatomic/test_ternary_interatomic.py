import pytest
from cifkit import Cif
from core.features.interatomic.ternary import (
    compute_features,
)

def test_compute_ternary_interatomic_feature(URhIn_cif):
    actual, _ = compute_features(URhIn_cif)
    expected = {
        "Entry": "URhIn",
        "Formula": "URhIn",
        "R": "U",
        "M": "Rh",
        "X": "In",
        "INT_distRR": 3.881,
        "INT_distMM": 3.881,
        "INT_distXX": 3.24367,
        "INT_distRM": 2.98347,
        "INT_distMX": 2.69678,
        "INT_distRX": 3.20977,
        "INT_Rsize": 1.377,
        "INT_Msize": 1.345,
        "INT_Xsize": 1.624,
        "INT_Rsize_by_Msize": 1.0237918215613384,
        "INT_Msize_by_Xsize": 0.8282019704433496,
        "INT_Rsize_by_Xsize": 0.8479064039408867,
        "INT_distRR_by2_byRsize": 1.4092229484386347,
        "INT_distMM_by2_byMsize": 1.4427509293680296,
        "INT_distXX_by2_byXsize": 0.9986668719211822,
        "INT_distRM_byRsizebyMsize": 1.0960580455547393,
        "INT_distMX_byMsizebyXsize": 0.9083125631525765,
        "INT_distRX_byRsizebyXsize": 1.0695668110629788,
        "INT_Rsize_ref": 1.6147054655661603,
        "INT_Msize_ref": 1.3687645344338397,
        "INT_Xsize_ref": 1.32801546556616,
        "INT_percent_diff_R_by_100": 0.17262561043294142,
        "INT_percent_diff_M_by_100": 0.017668798835568586,
        "INT_percent_diff_X_by_100": -0.18225648672034486,
        "INT_distRR_minus_ref_diff": 0.16789205587932984,
        "INT_distMM_minus_ref_diff": 0.2946330665118063,
        "INT_distXX_minus_ref_diff": 0.18116487462278216,
        "INT_distRM_minus_ref_diff": 0,
        "INT_distMX_minus_ref_diff": 0,
        "INT_distRX_minus_ref_diff": 0.08327217511284406,
        "INT_R_factor": 0.06332921478128069,
        "INT_UNI_shortest_homoatomic_dist": 3.24367,
        "INT_UNI_shortest_heteroatomic_dist": 2.69678,
        "INT_UNI_shortest_homoatomic_dist_by_2_by_atom_size": 0.9986668719211822,
        "INT_UNI_shortest_heteroatomic_dist_by_sum_of_atom_sizes": 0.9083125631525765,
        "INT_UNI_shortest_homoatomic_dist_by_2_by_refined_atom_size": 1.2212470728332812,
        "INT_UNI_shortest_heteroatomic_dist_by_sum_of_refined_atom_sizes": 1.0000000000000002,
        "INT_UNI_highest_refined_percent_diff_abs": 0.18225648672034486,
        "INT_UNI_lowest_refined_percent_diff_abs": 0.017668798835568586,
        "INT_UNI_refined_packing_efficiency": 0.60985,
    }

    for key, expected_value in expected.items():
        # For float
        if isinstance(expected_value, float):
            assert actual[key] == pytest.approx(expected_value, abs=0.001)
        # For str, integer, etc.
        else:
            assert actual[key] == expected_value
