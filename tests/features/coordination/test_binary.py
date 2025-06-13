import numpy as np
import pytest

from SAF.features.coordination.binary import compute_features


def test_features(Th7Rh3_cif):
    result = compute_features(Th7Rh3_cif)
    expected = {
        "CN_AVG_coordination_number": 13.5,
        "CN_AVG_A_atom_count": 10.75,
        "CN_AVG_B_atom_count": 2.75,
        "CN_AVG_polyhedron_volume": 111.40475,
        "CN_AVG_central_atom_to_center_of_mass_dist": 0.15425,
        "CN_AVG_number_of_edges": 34.5,
        "CN_AVG_number_of_faces": 23.0,
        "CN_AVG_shortest_distance_to_face": 2.56825,
        "CN_AVG_shortest_distance_to_edge": 2.61,
        "CN_AVG_volume_of_inscribed_sphere": 75.8885,
        "CN_AVG_packing_efficiency": 0.65125,
        "CN_MIN_coordination_number": 13.5,
        "CN_MIN_A_atom_count": 10.75,
        "CN_MIN_B_atom_count": 2.75,
        "CN_MIN_polyhedron_volume": 111.40475,
        "CN_MIN_central_atom_to_center_of_mass_dist": 0.15425,
        "CN_MIN_number_of_edges": 34.5,
        "CN_MIN_number_of_faces": 23.0,
        "CN_MIN_shortest_distance_to_face": 2.56825,
        "CN_MIN_shortest_distance_to_edge": 2.61,
        "CN_MIN_volume_of_inscribed_sphere": 75.8885,
        "CN_MIN_packing_efficiency": 0.65125,
        "CN_MAX_coordination_number": 13.5,
        "CN_MAX_A_atom_count": 10.75,
        "CN_MAX_B_atom_count": 2.75,
        "CN_MAX_polyhedron_volume": 111.40475,
        "CN_MAX_central_atom_to_center_of_mass_dist": 0.15425,
        "CN_MAX_number_of_edges": 34.5,
        "CN_MAX_number_of_faces": 23.0,
        "CN_MAX_shortest_distance_to_face": 2.56825,
        "CN_MAX_shortest_distance_to_edge": 2.61,
        "CN_MAX_volume_of_inscribed_sphere": 75.8885,
        "CN_MAX_packing_efficiency": 0.65125,
    }

    for key in result:
        assert result[key] == pytest.approx(expected[key], abs=0.01)
