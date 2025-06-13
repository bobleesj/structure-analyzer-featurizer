import pytest

from SAF.features.wyc.ternary import compute_features


def test_compute_features_ThSb(URhIn_cif):
    # Let R = U, M = Rh, X = In
    wyk_actual, wyk_uni_actual = compute_features(URhIn_cif)
    expected = {
        "WYK_R_lowest_wyckoff": 3,
        "WYK_M_lowest_wyckoff": 1,
        "WYK_X_lowest_wyckoff": 3,
        "WYK_identical_lowest_wyckoff_count": 1,
        "WYK_R_sites_total": 1,
        "WYK_M_sites_total": 2,
        "WYK_X_sites_total": 1,
        "WYK_R_multiplicity_total": 3,
        "WYK_M_multiplicity_total": 3,
        "WYK_X_multiplicity_total": 3,
    }
    uni_expected = {"UNI_WYK_lowest_wyckoff": 1}
    assert wyk_actual == expected
    assert wyk_uni_actual == uni_expected
