import pytest

from SAF.features.interatomic.binary import compute_features


def test_binary_test(ThSb_cif):
    elements = ["Th", "Sb"]
    actual, _ = compute_features(ThSb_cif, True, elements)
    expected = {
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
        "INT_UNI_refined_packing_efficiency": 0.70785,
    }

    for key, expected_value in expected.items():
        # For float
        if isinstance(expected_value, float):
            assert actual[key] == pytest.approx(expected_value, abs=0.001)
        # For str, integer, etc.
        else:
            assert actual[key] == expected_value
