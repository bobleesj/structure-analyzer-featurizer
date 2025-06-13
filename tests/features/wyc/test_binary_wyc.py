import pytest

from SAF.features.wyc.binary import compute_features


def test_compute_features_ThSb(ThSb_cif):
    result, uni_result = compute_features(ThSb_cif)
    expected = {
        "WYK_A_lowest_wyckoff": 1,
        "WYK_B_lowest_wyckoff": 1,
        "WYK_identical_lowest_wyckoff_count": 2,
        "WYK_A_sites_total": 1,
        "WYK_B_sites_total": 1,
        "WYK_A_multiplicity_total": 1,
        "WYK_B_multiplicity_total": 1,
    }
    uni_expected = {
        "UNI_WYK_lowest_wyckoff": 1,
    }
    assert result == expected
    assert uni_result == uni_expected


def test_compute_features_Th7Rh3(Th7Rh3_cif):
    result, uni_result = compute_features(Th7Rh3_cif)
    expected = {
        "WYK_A_lowest_wyckoff": 2,
        "WYK_B_lowest_wyckoff": 6,
        "WYK_identical_lowest_wyckoff_count": 1,
        "WYK_A_sites_total": 3,
        "WYK_B_sites_total": 1,
        "WYK_A_multiplicity_total": 14,
        "WYK_B_multiplicity_total": 6,
    }
    uni_expected = {"UNI_WYK_lowest_wyckoff": 2}
    assert result == expected
    assert uni_result == uni_expected
