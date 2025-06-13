from SAF.features.environment.util import (
    count_first_second_min_dist
)

def get_first_5_each(connections):
    return {k: v[:5] for k, v in list(connections.items())[:5]}


def test_count_first_second_min_dist(ThSb_cif):
    connections = ThSb_cif.connections
    # Print the first 10 connections for debugging, get the dictionary items
    result = get_first_5_each(connections)
    print(result)
    assert result == {'Sb1': [('Th1', 3.332, [-1.924, 1.924, -1.923], [-3.847, 0.0, 0.0]), ('Th1', 3.332, [-1.924, 1.924, -1.923], [-3.847, 3.847, -3.847]), ('Th1', 3.332, [-1.924, 1.924, -1.923], [-3.847, 0.0, -3.847]), ('Th1', 3.332, [-1.924, 1.924, -1.923], [-0.0, 3.847, 0.0]), ('Th1', 3.332, [-1.924, 1.924, -1.923], [0.0, 0.0, -3.847])], 'Th1': [('Sb1', 3.332, [0.0, 0.0, 0.0], [1.924, 1.924, -1.923]), ('Sb1', 3.332, [0.0, 0.0, 0.0], [-1.923, -1.923, -1.923]), ('Sb1', 3.332, [0.0, 0.0, 0.0], [-1.924, 1.924, -1.923]), ('Sb1', 3.332, [0.0, 0.0, 0.0], [-1.924, -1.924, 1.923]), ('Sb1', 3.332, [0.0, 0.0, 0.0], [1.924, -1.924, 1.923])]}
    # # result = count_first_second_min_dist(connections)
    # expected = {
    #     "Th": {
    #         "shortest_dist": 3.847,
    #         "second_shortest_dist": 4.0,
    #         "shortest_dist_count": 8,
    #         "second_shortest_dist_count": 6
    #     },
    #     "Sb": {
    #         "shortest_dist": 3.332,
    #         "second_shortest_dist": 3.5,
    #         "shortest_dist_count": 8,
    #         "second_shortest_dist_count": 6
    #     }
    # }
    
    # assert result == expected, f"Expected {expected}, but got {result}"