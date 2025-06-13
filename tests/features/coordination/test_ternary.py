import numpy as np
import pytest

from SAF.features.coordination.ternary import compute_features


def test_features(URhIn_cif):
    result = compute_features(URhIn_cif)
    expected = {
        "CN_AVG_coordination_number": 11.5,
        "CN_AVG_R_atom_count": 4.5,
        "CN_AVG_M_atom_count": 2.25,
        "CN_AVG_X_atom_count": 4.75,
        "CN_AVG_polyhedron_volume": 67.79050000000001,
        "CN_AVG_central_atom_to_center_of_mass_dist": 0.07925000000000001,
        "CN_AVG_number_of_edges": 28.5,
        "CN_AVG_number_of_faces": 19.0,
        "CN_AVG_shortest_distance_to_face": 2.158375,
        "CN_AVG_shortest_distance_to_edge": 2.238625,
        "CN_AVG_volume_of_inscribed_sphere": 44.27,
        "CN_AVG_packing_efficiency": 0.64575,
        "CN_MIN_coordination_number": 10.75,
        "CN_MIN_R_atom_count": 3.75,
        "CN_MIN_M_atom_count": 2.25,
        "CN_MIN_X_atom_count": 4.75,
        "CN_MIN_polyhedron_volume": 60.91375,
        "CN_MIN_central_atom_to_center_of_mass_dist": 0.04225,
        "CN_MIN_number_of_edges": 26.25,
        "CN_MIN_number_of_faces": 17.5,
        "CN_MIN_shortest_distance_to_face": 2.0749999999999997,
        "CN_MIN_shortest_distance_to_edge": 2.14975,
        "CN_MIN_volume_of_inscribed_sphere": 38.59575,
        "CN_MIN_packing_efficiency": 0.62875,
        "CN_MAX_coordination_number": 12.25,
        "CN_MAX_R_atom_count": 5.25,
        "CN_MAX_M_atom_count": 2.25,
        "CN_MAX_X_atom_count": 4.75,
        "CN_MAX_polyhedron_volume": 74.66725,
        "CN_MAX_central_atom_to_center_of_mass_dist": 0.11625,
        "CN_MAX_number_of_edges": 30.75,
        "CN_MAX_number_of_faces": 20.5,
        "CN_MAX_shortest_distance_to_face": 2.2417499999999997,
        "CN_MAX_shortest_distance_to_edge": 2.3274999999999997,
        "CN_MAX_volume_of_inscribed_sphere": 49.94425,
        "CN_MAX_packing_efficiency": 0.66275,
    }
    for key in result:
        assert result[key] == pytest.approx(expected[key], abs=0.01)
