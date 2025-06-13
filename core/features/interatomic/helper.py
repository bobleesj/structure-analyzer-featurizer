def get_bond_distances_by_labels(min_dists: dict[str, float], bond_labels: list[str]) -> dict[str, float]:
    """Extract bond distances for specified labels from a dictionary of minimum distances."""
    return {key: min_dists[key] for key in bond_labels}

def get_min_from_dists(dists: dict[str, float]) -> float:
    """Get the minimum value from a dictionary of distances."""
    return min(dists.values())

