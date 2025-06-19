from SAF.features.wyc.quaternary import compute_features


def test_compute_features_Th4RhInGe4(Tb4RhInGe4_cif, TbRhInGe_elements_tuple):
    # Let A = Tb, B = Rh, C = In, D = Ge
    wyk_actual, wyk_uni_actual = compute_features(Tb4RhInGe4_cif, TbRhInGe_elements_tuple)
    expected = {
        "WYK_A_lowest_wyckoff": 4,
        "WYK_B_lowest_wyckoff": 4,
        "WYK_C_lowest_wyckoff": 2,
        "WYK_D_lowest_wyckoff": 4,
        "WYK_identical_lowest_wyckoff_count": 1,
        "WYK_A_sites_total": 4,
        "WYK_B_sites_total": 1,
        "WYK_C_sites_total": 2,
        "WYK_D_sites_total": 4,
        "WYK_A_multiplicity_total": 16,
        "WYK_B_multiplicity_total": 4,
        "WYK_C_multiplicity_total": 4,
        "WYK_D_multiplicity_total": 16,
    }
    uni_expected = {"UNI_WYK_lowest_wyckoff": 2}

    print("WYK Actual:", wyk_actual)
    print("WYK Uni Actual:", wyk_uni_actual)
    assert wyk_actual == expected
    assert wyk_uni_actual == uni_expected
