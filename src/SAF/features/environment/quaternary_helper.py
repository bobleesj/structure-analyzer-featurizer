from cifkit.utils import string_parser

from SAF.features.environment.util import _get_site_labels_per_element, count_first_second_min_dist, extract_best_labels


def compute_homoatomic_dist_by_site_shortest_dist(connections, A_best_label, B_best_label, C_best_label, D_best_label):
    """Compute the shortest homoatomic distances normalized by the shortest
    distance encountered at the best site for each element."""
    A = string_parser.get_atom_type_from_label(A_best_label)
    B = string_parser.get_atom_type_from_label(B_best_label)
    C = string_parser.get_atom_type_from_label(C_best_label)
    D = string_parser.get_atom_type_from_label(D_best_label)
    A_homoatomic_shortest_dist = float("inf")
    B_homoatomic_shortest_dist = float("inf")
    C_homoatomic_shortest_dist = float("inf")
    D_homoatomic_shortest_dist = float("inf")
    A_min_dist = float("inf")
    B_min_dist = float("inf")
    C_min_dist = float("inf")
    D_min_dist = float("inf")
    # Process each site
    for site_label, site_connections in connections.items():
        # Compute the shortest distance at this site
        current_min_dist = min([dist for _, dist, _, _ in site_connections])
        # Update the minimum distances for A, B, C, and D if this is their best site
        if site_label == A_best_label:
            A_min_dist = current_min_dist
            A_homoatomic_shortest_dist = min([dist for label, dist, _, _ in site_connections if label.startswith(A)])
        if site_label == B_best_label:
            B_min_dist = current_min_dist
            B_homoatomic_shortest_dist = min([dist for label, dist, _, _ in site_connections if label.startswith(B)])
        if site_label == C_best_label:
            C_min_dist = current_min_dist
            C_homoatomic_shortest_dist = min([dist for label, dist, _, _ in site_connections if label.startswith(C)])
        if site_label == D_best_label:
            D_min_dist = current_min_dist
            D_homoatomic_shortest_dist = min([dist for label, dist, _, _ in site_connections if label.startswith(D)])
    # Normalize the shortest distances by the shortest distances at the best sites
    A_homoatomic_dist_by_shortest_dist = A_homoatomic_shortest_dist / A_min_dist
    B_homoatomic_dist_by_shortest_dist = B_homoatomic_shortest_dist / B_min_dist
    C_homoatomic_dist_by_shortest_dist = C_homoatomic_shortest_dist / C_min_dist
    D_homoatomic_dist_by_shortest_dist = D_homoatomic_shortest_dist / D_min_dist
    return (
        A_homoatomic_dist_by_shortest_dist,
        B_homoatomic_dist_by_shortest_dist,
        C_homoatomic_dist_by_shortest_dist,
        D_homoatomic_dist_by_shortest_dist,
    )


def compute_avg_homoatomic_dist_by_site_shortest_dist(connections, A, B, C, D):
    """Compute the average of the homoatomic distances normalized by the
    shortest distance encountered at each site for four distinct element types
    within a given set of connections."""
    element_to_site_labels = _get_site_labels_per_element(connections)
    A_total_homoatomic_dist_by_shortest_dist = 0.0
    B_total_homoatomic_dist_by_shortest_dist = 0.0
    C_total_homoatomic_dist_by_shortest_dist = 0.0
    D_total_homoatomic_dist_by_shortest_dist = 0.0
    for site_label, site_connections in connections.items():
        shortest_dist_per_site = site_connections[0][1]
        for connection in site_connections:
            other_label, dist, _, _ = connection
            if site_label.startswith(A) and other_label.startswith(A):
                A_total_homoatomic_dist_by_shortest_dist += dist / shortest_dist_per_site
                break
            if site_label.startswith(B) and other_label.startswith(B):
                B_total_homoatomic_dist_by_shortest_dist += dist / shortest_dist_per_site
                break
            if site_label.startswith(C) and other_label.startswith(C):
                C_total_homoatomic_dist_by_shortest_dist += dist / shortest_dist_per_site
                break
            if site_label.startswith(D) and other_label.startswith(D):
                D_total_homoatomic_dist_by_shortest_dist += dist / shortest_dist_per_site
                break
    A_avg_homoatomic_dist_by_shortest_dist = A_total_homoatomic_dist_by_shortest_dist / len(element_to_site_labels[A])
    B_avg_homoatomic_dist_by_shortest_dist = B_total_homoatomic_dist_by_shortest_dist / len(element_to_site_labels[B])
    C_avg_homoatomic_dist_by_shortest_dist = C_total_homoatomic_dist_by_shortest_dist / len(element_to_site_labels[C])
    D_avg_homoatomic_dist_by_shortest_dist = D_total_homoatomic_dist_by_shortest_dist / len(element_to_site_labels[D])
    return (
        A_avg_homoatomic_dist_by_shortest_dist,
        B_avg_homoatomic_dist_by_shortest_dist,
        C_avg_homoatomic_dist_by_shortest_dist,
        D_avg_homoatomic_dist_by_shortest_dist,
    )


def get_A_and_B_and_C_and_D_count_in_best_label_per_element(connections, A, B, C, D):
    """Compute the occurrences of element types A, B, C, D at the shortest
    distances within their respective best labeled site for each element.

    The best site label is determined with the label with the shortest
    distance pair.
    """
    A_count_at_A_shortest_dist = 0
    A_count_at_B_shortest_dist = 0
    A_count_at_C_shortest_dist = 0
    A_count_at_D_shortest_dist = 0
    B_count_at_A_shortest_dist = 0
    B_count_at_B_shortest_dist = 0
    B_count_at_C_shortest_dist = 0
    B_count_at_D_shortest_dist = 0
    C_count_at_A_shortest_dist = 0
    C_count_at_B_shortest_dist = 0
    C_count_at_C_shortest_dist = 0
    C_count_at_D_shortest_dist = 0
    D_count_at_A_shortest_dist = 0
    D_count_at_B_shortest_dist = 0
    D_count_at_C_shortest_dist = 0
    D_count_at_D_shortest_dist = 0
    dist_count_per_label = count_first_second_min_dist(connections)
    best_label_dict = extract_best_labels(dist_count_per_label)
    best_A_site_label = best_label_dict[A]["best_label"]
    best_A_shortest_dist = best_label_dict[A]["best_label_details"]["shortest_dist"]
    best_B_site_label = best_label_dict[B]["best_label"]
    best_B_shortest_dist = best_label_dict[B]["best_label_details"]["shortest_dist"]
    best_C_site_label = best_label_dict[C]["best_label"]
    best_C_shortest_dist = best_label_dict[C]["best_label_details"]["shortest_dist"]
    best_D_site_label = best_label_dict[D]["best_label"]
    best_D_shortest_dist = best_label_dict[D]["best_label_details"]["shortest_dist"]
    for connection in connections[best_A_site_label]:
        other_label, dist, _, _ = connection
        if dist == best_A_shortest_dist:
            if other_label.startswith(A):
                A_count_at_A_shortest_dist += 1
            if other_label.startswith(B):
                B_count_at_A_shortest_dist += 1
            if other_label.startswith(C):
                C_count_at_A_shortest_dist += 1
            if other_label.startswith(D):
                D_count_at_A_shortest_dist += 1
    for connection in connections[best_B_site_label]:
        other_label, dist, _, _ = connection
        if dist == best_B_shortest_dist:
            if other_label.startswith(A):
                A_count_at_B_shortest_dist += 1
            if other_label.startswith(B):
                B_count_at_B_shortest_dist += 1
            if other_label.startswith(C):
                C_count_at_B_shortest_dist += 1
            if other_label.startswith(D):
                D_count_at_B_shortest_dist += 1
    for connection in connections[best_C_site_label]:
        other_label, dist, _, _ = connection
        if dist == best_C_shortest_dist:
            if other_label.startswith(A):
                A_count_at_C_shortest_dist += 1
            if other_label.startswith(B):
                B_count_at_C_shortest_dist += 1
            if other_label.startswith(C):
                C_count_at_C_shortest_dist += 1
            if other_label.startswith(D):
                D_count_at_C_shortest_dist += 1
    for connection in connections[best_D_site_label]:
        other_label, dist, _, _ = connection
        if dist == best_D_shortest_dist:
            if other_label.startswith(A):
                A_count_at_D_shortest_dist += 1
            if other_label.startswith(B):
                B_count_at_D_shortest_dist += 1
            if other_label.startswith(C):
                C_count_at_D_shortest_dist += 1
            if other_label.startswith(D):
                D_count_at_D_shortest_dist += 1
    return (
        A_count_at_A_shortest_dist,
        A_count_at_B_shortest_dist,
        A_count_at_C_shortest_dist,
        A_count_at_D_shortest_dist,
        B_count_at_A_shortest_dist,
        B_count_at_B_shortest_dist,
        B_count_at_C_shortest_dist,
        B_count_at_D_shortest_dist,
        C_count_at_A_shortest_dist,
        C_count_at_B_shortest_dist,
        C_count_at_C_shortest_dist,
        C_count_at_D_shortest_dist,
        D_count_at_A_shortest_dist,
        D_count_at_B_shortest_dist,
        D_count_at_C_shortest_dist,
        D_count_at_D_shortest_dist,
    )


def get_avg_A_and_B_and_C_and_D_count_in_per_element(connections, A, B, C, D):
    """Compute the occurrences of element types A, B, C, D at the shortest
    distances within their respective site for all site labels."""
    A_total_count_at_A_shortest_dist = 0
    A_total_count_at_B_shortest_dist = 0
    A_total_count_at_C_shortest_dist = 0
    A_total_count_at_D_shortest_dist = 0
    B_total_count_at_A_shortest_dist = 0
    B_total_count_at_B_shortest_dist = 0
    B_total_count_at_C_shortest_dist = 0
    B_total_count_at_D_shortest_dist = 0
    C_total_count_at_A_shortest_dist = 0
    C_total_count_at_B_shortest_dist = 0
    C_total_count_at_C_shortest_dist = 0
    C_total_count_at_D_shortest_dist = 0
    D_total_count_at_A_shortest_dist = 0
    D_total_count_at_B_shortest_dist = 0
    D_total_count_at_C_shortest_dist = 0
    D_total_count_at_D_shortest_dist = 0
    dist_count_per_label = count_first_second_min_dist(connections)
    best_labels = extract_best_labels(dist_count_per_label)
    A_site_label_count = best_labels[A]["label_count"]
    B_site_label_count = best_labels[B]["label_count"]
    C_site_label_count = best_labels[C]["label_count"]
    D_site_label_count = best_labels[D]["label_count"]

    for site_label, connection_data in connections.items():
        parsed_element = string_parser.get_atom_type_from_label(site_label)
        shortest_dist_per_site_label = dist_count_per_label[site_label]["shortest_dist"]

        for connection in connection_data:
            other_label, dist, _, _ = connection
            if parsed_element == A and dist == shortest_dist_per_site_label:
                if other_label.startswith(A):
                    A_total_count_at_A_shortest_dist += 1
                if other_label.startswith(B):
                    B_total_count_at_A_shortest_dist += 1
                if other_label.startswith(C):
                    C_total_count_at_A_shortest_dist += 1
                if other_label.startswith(D):
                    D_total_count_at_A_shortest_dist += 1
            if parsed_element == B and dist == shortest_dist_per_site_label:
                if other_label.startswith(A):
                    A_total_count_at_B_shortest_dist += 1
                if other_label.startswith(B):
                    B_total_count_at_B_shortest_dist += 1
                if other_label.startswith(C):
                    C_total_count_at_B_shortest_dist += 1
                if other_label.startswith(D):
                    D_total_count_at_B_shortest_dist += 1
            if parsed_element == C and dist == shortest_dist_per_site_label:
                if other_label.startswith(A):
                    A_total_count_at_C_shortest_dist += 1
                if other_label.startswith(B):
                    B_total_count_at_C_shortest_dist += 1
                if other_label.startswith(C):
                    C_total_count_at_C_shortest_dist += 1
                if other_label.startswith(D):
                    D_total_count_at_C_shortest_dist += 1
            if parsed_element == D and dist == shortest_dist_per_site_label:
                if other_label.startswith(A):
                    A_total_count_at_D_shortest_dist += 1
                if other_label.startswith(B):
                    B_total_count_at_D_shortest_dist += 1
                if other_label.startswith(C):
                    C_total_count_at_D_shortest_dist += 1
                if other_label.startswith(D):
                    D_total_count_at_D_shortest_dist += 1

    A_avg_count_at_A = A_total_count_at_A_shortest_dist / A_site_label_count
    A_avg_count_at_B = A_total_count_at_B_shortest_dist / B_site_label_count
    A_avg_count_at_C = A_total_count_at_C_shortest_dist / C_site_label_count
    A_avg_count_at_D = A_total_count_at_D_shortest_dist / D_site_label_count
    B_avg_count_at_A = B_total_count_at_A_shortest_dist / A_site_label_count
    B_avg_count_at_B = B_total_count_at_B_shortest_dist / B_site_label_count
    B_avg_count_at_C = B_total_count_at_C_shortest_dist / C_site_label_count
    B_avg_count_at_D = B_total_count_at_D_shortest_dist / D_site_label_count
    C_avg_count_at_A = C_total_count_at_A_shortest_dist / A_site_label_count
    C_avg_count_at_B = C_total_count_at_B_shortest_dist / B_site_label_count
    C_avg_count_at_C = C_total_count_at_C_shortest_dist / C_site_label_count
    C_avg_count_at_D = C_total_count_at_D_shortest_dist / D_site_label_count
    D_avg_count_at_A = D_total_count_at_A_shortest_dist / A_site_label_count
    D_avg_count_at_B = D_total_count_at_B_shortest_dist / B_site_label_count
    D_avg_count_at_C = D_total_count_at_C_shortest_dist / C_site_label_count
    D_avg_count_at_D = D_total_count_at_D_shortest_dist / D_site_label_count

    return (
        A_avg_count_at_A,
        A_avg_count_at_B,
        A_avg_count_at_C,
        A_avg_count_at_D,
        B_avg_count_at_A,
        B_avg_count_at_B,
        B_avg_count_at_C,
        B_avg_count_at_D,
        C_avg_count_at_A,
        C_avg_count_at_B,
        C_avg_count_at_C,
        C_avg_count_at_D,
        D_avg_count_at_A,
        D_avg_count_at_B,
        D_avg_count_at_C,
        D_avg_count_at_D,
    )
