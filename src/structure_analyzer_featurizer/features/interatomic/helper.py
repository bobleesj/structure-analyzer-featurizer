def get_bond_distances_by_labels(min_dists: dict[str, float], bond_labels: list[str]) -> dict[str, float]:
    """Extract bond distances for specified labels from a dictionary of minimum
    distances."""
    return {key: min_dists[key] for key in bond_labels}


def get_min_from_dists(dists: dict[str, float]) -> float:
    """Get the minimum value from a dictionary of distances."""
    return min(dists.values())


def get_shortest_homo_key(min_bond_dists, shortest_homoatomic_dist):
    return [k for k, v in min_bond_dists.items() if v == shortest_homoatomic_dist][0]


def get_shortest_hetero_key(min_bond_dists, shortest_heteroatomic_dist):
    return [k for k, v in min_bond_dists.items() if v == shortest_heteroatomic_dist][0]


def get_highest_refined_percent_diff(percent_diffs):
    return max([abs(p) for p in percent_diffs])


def get_lowest_refined_percent_diff(percent_diffs):
    return min([abs(p) for p in percent_diffs])


def get_shortest_homo_heteroatomic_features(
    shortest_homoatomic_dist,
    shortest_homo_key,
    shortest_heteroatomic_dist,
    shortest_hetero_key,
    rad_dict,
    refined_rad_dict,
):
    return {
        "shortest_homoatomic_dist_by_2_by_atom_size": (shortest_homoatomic_dist / 2) / rad_dict[shortest_homo_key],
        "shortest_homoatomic_dist_by_2_by_refined_atom_sizes": (shortest_homoatomic_dist / 2) / refined_rad_dict[shortest_homo_key],
        "shortest_heteroatomic_dist_by_sum_of_atom_sizes": shortest_heteroatomic_dist / rad_dict[shortest_hetero_key],
        "shortest_heteroatomic_dist_by_refined_atom_sizes": shortest_heteroatomic_dist / refined_rad_dict[shortest_hetero_key],
    }
