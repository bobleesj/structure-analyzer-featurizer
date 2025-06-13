import itertools
from typing import Dict, Tuple


def get_min_distances_by_labels(
    shortest_bond_pair_distance: Dict[Tuple[str, str], float],
    elements: list[str],
    labels: list[str] = None,
) -> dict[str, float]:
    """Get bond distances using symbolic labels (like RR, RX, MX) for arbitrary
    elements.

    Parameters
    ----------
        shortest_bond_pair_distance: dict of bond distances keyed by (element1, element2)
        elements: list of actual element symbols
        labels: optional symbolic labels (e.g., ['R', 'M', 'X']) to use for display keys

    Returns
    -------
        Dict[str, float] with symbolic pair keys

    Examples
    --------
    >>> bond_distances = {
    ...     ('Th', 'Th'): 1.1,
    ...     ('Os', 'Os'): 1.2,
    ...     ('Th', 'Os'): 1.3,
    ... }
    >>> get_shortest_bond_distances(bond_distances, ['Th', 'Os'], labels=['A', 'B'])
    {'AA': 1.1, 'BB': 1.2, 'AB': 1.3}
    """
    if labels is None:
        labels = elements

    distances = {}
    for elem1, elem2 in itertools.combinations_with_replacement(elements, 2):
        label1 = labels[elements.index(elem1)]
        label2 = labels[elements.index(elem2)]
        key = f"{label1}{label2}"

        dist = shortest_bond_pair_distance.get((elem1, elem2)) or shortest_bond_pair_distance.get((elem2, elem1))
        if dist is None:
            raise KeyError(f"Missing bond distance for pair ({elem1}, {elem2})")
        distances[key] = dist

    return distances
