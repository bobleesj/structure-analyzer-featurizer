import numpy as np
import pytest

from SAF.features.coordination.quaternary import compute_features


def test_features(Tb4RhInGe4_cif):
    result = compute_features(Tb4RhInGe4_cif)
    expected = {
        "CN_AVG_coordination_number": 13.068181818181818,
        "CN_AVG_A_atom_count": 6.9772727272727275,
        "CN_AVG_B_atom_count": 1.0909090909090908,
        "CN_AVG_C_atom_count": 1.2727272727272727,
        "CN_AVG_D_atom_count": 3.727272727272727,
        "CN_AVG_polyhedron_volume": 85.20697727272726,
        "CN_AVG_central_atom_to_center_of_mass_dist": 0.09595454545454546,
        "CN_AVG_number_of_edges": 33.20454545454545,
        "CN_AVG_number_of_faces": 22.136363636363637,
        "CN_AVG_shortest_distance_to_face": 2.3147045454545454,
        "CN_AVG_shortest_distance_to_edge": 2.3177499999999998,
        "CN_AVG_volume_of_inscribed_sphere": 55.812318181818185,
        "CN_AVG_packing_efficiency": 0.6347499999999999,
        "CN_MIN_coordination_number": 12.818181818181818,
        "CN_MIN_A_atom_count": 6.909090909090909,
        "CN_MIN_B_atom_count": 1.0909090909090908,
        "CN_MIN_C_atom_count": 1.0909090909090908,
        "CN_MIN_D_atom_count": 3.727272727272727,
        "CN_MIN_polyhedron_volume": 82.86009090909091,
        "CN_MIN_central_atom_to_center_of_mass_dist": 0.09081818181818181,
        "CN_MIN_number_of_edges": 32.45454545454545,
        "CN_MIN_number_of_faces": 21.636363636363637,
        "CN_MIN_shortest_distance_to_face": 2.2578181818181817,
        "CN_MIN_shortest_distance_to_edge": 2.225818181818182,
        "CN_MIN_volume_of_inscribed_sphere": 53.12227272727273,
        "CN_MIN_packing_efficiency": 0.6080909090909091,
        "CN_MAX_coordination_number": 13.272727272727273,
        "CN_MAX_A_atom_count": 7.0,
        "CN_MAX_B_atom_count": 1.0909090909090908,
        "CN_MAX_C_atom_count": 1.4545454545454546,
        "CN_MAX_D_atom_count": 3.727272727272727,
        "CN_MAX_polyhedron_volume": 87.19936363636363,
        "CN_MAX_central_atom_to_center_of_mass_dist": 0.11136363636363637,
        "CN_MAX_number_of_edges": 33.81818181818182,
        "CN_MAX_number_of_faces": 22.545454545454547,
        "CN_MAX_shortest_distance_to_face": 2.344727272727272,
        "CN_MAX_shortest_distance_to_edge": 2.3777272727272725,
        "CN_MAX_volume_of_inscribed_sphere": 57.506181818181815,
        "CN_MAX_packing_efficiency": 0.644,
    }
    for key in result:
        assert result[key] == pytest.approx(expected[key], abs=0.01)
