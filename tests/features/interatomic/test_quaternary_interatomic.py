import numpy as np
import pytest

from SAF.features.interatomic.quaternary import compute_features


def test_compute_features(Tb4RhInGe4_cif, TbRhInGe_elements_tuple):
    actual, _ = compute_features(Tb4RhInGe4_cif, True, TbRhInGe_elements_tuple)
    expected = {
        "Entry": "Tb4RhInGe4",
        "Formula": "Tb4RhInGe4",
        "Structure": "Tb4RhInGe4",
        "A": "Tb",
        "B": "Rh",
        "C": "In",
        "D": "Ge",
        "INT_AA_dist": 3.538,
        "INT_BB_dist": 3.148,
        "INT_CC_dist": 4.264,
        "INT_DD_dist": 2.596,
        "INT_AB_dist": 3.076,
        "INT_AC_dist": 3.367,
        "INT_AD_dist": 2.917,
        "INT_BC_dist": 4.711,
        "INT_BD_dist": 2.47,
        "INT_CD_dist": 2.818,
        "INT_Asize": 1.764,
        "INT_Bsize": 1.345,
        "INT_Csize": 1.624,
        "INT_Dsize": 1.225,
        "INT_Asize_by_Bsize": 1.3115241635687733,
        "INT_Bsize_by_Csize": 0.8282019704433496,
        "INT_Csize_by_Dsize": 1.3257142857142856,
        "INT_Asize_by_Csize": 1.086206896551724,
        "INT_Asize_by_Dsize": 1.44,
        "INT_Bsize_by_Dsize": 1.0979591836734692,
        "INT_AA_dist_by_2_by_Asize": 1.0028344671201814,
        "INT_BB_dist_by_2_by_Bsize": 1.1702602230483272,
        "INT_CC_dist_by_2_by_Csize": 1.312807881773399,
        "INT_DD_dist_by_2_by_Dsize": 1.059591836734694,
        "INT_AB_dist_by_ABsizes": 0.9893856545513027,
        "INT_AC_dist_by_ACsizes": 0.9938016528925621,
        "INT_AD_dist_by_ADsizes": 0.9759116761458682,
        "INT_BC_dist_by_BCsizes": 1.5867295385651734,
        "INT_BD_dist_by_BDsizes": 0.961089494163424,
        "INT_CD_dist_by_CDsizes": 0.9891189891189891,
        "INT_Asize_ref": np.float64(1.6862073857087099),
        "INT_Bsize_ref": np.float64(1.4201916565448087),
        "INT_Csize_ref": np.float64(1.6861073857088038),
        "INT_Dsize_ref": np.float64(1.1604492903475334),
        "INT_percent_diff_A_by_100": np.float64(-0.04410012148032321),
        "INT_percent_diff_B_by_100": np.float64(0.05590457735673513),
        "INT_percent_diff_C_by_100": np.float64(0.038243464106406215),
        "INT_percent_diff_D_by_100": np.float64(-0.05269445685915647),
        "INT_AA_minus_ref_diff": np.float64(0.04680193006856418),
        "INT_BB_minus_ref_diff": np.float64(0.0977181343425612),
        "INT_CC_minus_ref_diff": np.float64(0.20914287724727781),
        "INT_DD_minus_ref_diff": np.float64(0.10597127091869539),
        "INT_AB_minus_ref_diff": np.float64(-0.009882653528452056),
        "INT_AC_minus_ref_diff": np.float64(-0.0015784886894902542),
        "INT_AD_minus_ref_diff": np.float64(0.02411495507156549),
        "INT_BC_minus_ref_diff": np.float64(0.3406285200056013),
        "INT_BD_minus_ref_diff": np.float64(-0.04479390562442993),
        "INT_CD_minus_ref_diff": np.float64(-0.010133667869530575),
        "INT_R_factor": np.float64(0.00930941081455393),
        "INT_UNI_shortest_homoatomic_dist": 2.596,
        "INT_UNI_shortest_heteroatomic_dist": 2.47,
        "INT_UNI_shortest_homoatomic_dist_by_2_by_atom_size": 1.059591836734694,
        "INT_UNI_shortest_heteroatomic_dist_by_sum_of_atom_sizes": 0.961089494163424,
        "INT_UNI_shortest_homoatomic_dist_by_2_by_refined_atom_size": np.float64(1.1185322881375306),
        "INT_UNI_shortest_heteroatomic_dist_by_sum_of_refined_atom_sizes": np.float64(0.9571265630634986),
        "INT_UNI_highest_refined_percent_diff_abs": np.float64(0.05590457735673513),
        "INT_UNI_lowest_refined_percent_diff_abs": np.float64(0.038243464106406215),
        "INT_UNI_refined_packing_efficiency": np.float64(0.64862),
    }
    for key, expected_value in expected.items():
        # For float
        if isinstance(expected_value, float):
            assert actual[key] == pytest.approx(expected_value, abs=0.001)
        # For str, integer, etc.
        else:
            assert actual[key] == expected_value
