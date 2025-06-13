import numpy as np

from SAF.features.environment.util import count_first_second_min_dist


def get_nearest_connections_no_coords(connections, count=20):
    """Return the first `count` connections for each site label, including only
    the element label and distance.

    This simplifies inspection/debugging.
    """
    return {k: [(elem, dist) for (elem, dist, *_) in v[:count]] for k, v in list(connections.items())[:count]}


def test_count_first_second_min_dist_binary(ThSb_cif):
    connections = ThSb_cif.connections
    first_second_min_dists = get_nearest_connections_no_coords(connections)
    assert first_second_min_dists == {
        "Sb1": [
            ("Th1", 3.332),
            ("Th1", 3.332),
            ("Th1", 3.332),
            ("Th1", 3.332),
            ("Th1", 3.332),
            ("Th1", 3.332),
            ("Th1", 3.332),
            ("Th1", 3.332),
            ("Sb1", 3.847),
            ("Sb1", 3.847),
            ("Sb1", 3.847),
            ("Sb1", 3.847),
            ("Sb1", 3.847),
            ("Sb1", 3.847),
            ("Sb1", 5.44),
            ("Sb1", 5.44),
            ("Sb1", 5.44),
            ("Sb1", 5.44),
            ("Sb1", 5.44),
            ("Sb1", 5.44),
        ],
        "Th1": [
            ("Sb1", 3.332),
            ("Sb1", 3.332),
            ("Sb1", 3.332),
            ("Sb1", 3.332),
            ("Sb1", 3.332),
            ("Sb1", 3.332),
            ("Sb1", 3.332),
            ("Sb1", 3.332),
            ("Th1", 3.847),
            ("Th1", 3.847),
            ("Th1", 3.847),
            ("Th1", 3.847),
            ("Th1", 3.847),
            ("Th1", 3.847),
            ("Th1", 5.44),
            ("Th1", 5.44),
            ("Th1", 5.44),
            ("Th1", 5.44),
            ("Th1", 5.44),
            ("Th1", 5.44),
        ],
    }
    first_second_min_dists = count_first_second_min_dist(connections)
    expected = {
        "Sb1": {
            "shortest_dist": np.float64(3.332),
            "second_shortest_dist": np.float64(3.847),
            "counts": {np.float64(3.332): 8, np.float64(3.847): 6},
        },
        "Th1": {
            "shortest_dist": np.float64(3.332),
            "second_shortest_dist": np.float64(3.847),
            "counts": {np.float64(3.332): 8, np.float64(3.847): 6},
        },
    }
    assert first_second_min_dists == expected


def test_count_first_second_min_dist_ternary(URhIn_cif):
    connections = URhIn_cif.connections
    # Print the first 10 connections for debugging, get the dictionary items
    first_second_min_dists = get_nearest_connections_no_coords(connections)
    print(first_second_min_dists)
    assert first_second_min_dists == {
        "In1": [
            ("Rh2", 2.697),
            ("Rh2", 2.697),
            ("Rh1", 2.852),
            ("Rh1", 2.852),
            ("U1", 3.21),
            ("U1", 3.21),
            ("In1", 3.244),
            ("In1", 3.244),
            ("U1", 3.294),
            ("U1", 3.294),
            ("U1", 3.294),
            ("U1", 3.294),
            ("In1", 3.881),
            ("In1", 3.881),
            ("Rh1", 4.705),
            ("Rh1", 4.705),
            ("Rh1", 4.816),
            ("Rh1", 4.817),
            ("Rh1", 4.817),
            ("Rh1", 4.817),
        ],
        "U1": [
            ("Rh1", 2.983),
            ("Rh1", 2.983),
            ("Rh1", 2.983),
            ("Rh1", 2.984),
            ("Rh2", 3.046),
            ("In1", 3.21),
            ("In1", 3.21),
            ("In1", 3.294),
            ("In1", 3.294),
            ("In1", 3.294),
            ("In1", 3.294),
            ("U1", 3.881),
            ("U1", 3.881),
            ("U1", 3.925),
            ("U1", 3.925),
            ("U1", 3.925),
            ("U1", 3.925),
            ("Rh2", 4.43),
            ("Rh2", 4.934),
            ("Rh2", 4.934),
        ],
        "Rh1": [
            ("In1", 2.852),
            ("In1", 2.852),
            ("In1", 2.853),
            ("U1", 2.983),
            ("U1", 2.983),
            ("U1", 2.983),
            ("U1", 2.984),
            ("U1", 2.984),
            ("U1", 2.984),
            ("Rh1", 3.881),
            ("Rh1", 3.881),
            ("Rh1", 4.316),
            ("Rh1", 4.316),
            ("Rh1", 4.316),
            ("In1", 4.705),
            ("In1", 4.705),
            ("In1", 4.705),
            ("Rh2", 4.732),
            ("Rh2", 4.732),
            ("Rh2", 4.732),
        ],
        "Rh2": [
            ("In1", 2.697),
            ("In1", 2.697),
            ("In1", 2.697),
            ("In1", 2.697),
            ("In1", 2.697),
            ("In1", 2.697),
            ("U1", 3.046),
            ("U1", 3.046),
            ("U1", 3.046),
            ("Rh2", 3.881),
            ("Rh2", 3.881),
            ("U1", 4.43),
            ("U1", 4.43),
            ("U1", 4.43),
            ("Rh1", 4.732),
            ("Rh1", 4.732),
            ("Rh1", 4.732),
            ("Rh1", 4.732),
            ("Rh1", 4.732),
            ("Rh1", 4.732),
        ],
    }

    first_second_min_dists = count_first_second_min_dist(connections)
    assert first_second_min_dists == {
        "In1": {"shortest_dist": 2.697, "second_shortest_dist": 2.852, "counts": {2.697: 2, 2.852: 2}},
        "U1": {"shortest_dist": 2.983, "second_shortest_dist": 2.984, "counts": {2.983: 3, 2.984: 1}},
        "Rh1": {"shortest_dist": 2.852, "second_shortest_dist": 2.853, "counts": {2.852: 2, 2.853: 1}},
        "Rh2": {"shortest_dist": 2.697, "second_shortest_dist": 3.046, "counts": {2.697: 6, 3.046: 3}},
    }
