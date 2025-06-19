from cifkit import Cif

from SAF.features.environment.quaternary_helper import (
    compute_avg_homoatomic_dist_by_site_shortest_dist,
    compute_homoatomic_dist_by_site_shortest_dist,
    get_A_and_B_and_C_and_D_count_in_best_label_per_element,
    get_avg_A_and_B_and_C_and_D_count_in_per_element,
)
from SAF.features.environment.util import (
    count_first_second_min_dist,
    extract_avg_shortest_dist_with_tol,
    extract_best_labels,
    extract_shortest_dist_with_tol,
    get_avg_second_by_first_shortest_dist_ratio,
)


def compute_features(cif: Cif, elements):
    connections = cif.connections
    A, B, C, D = elements

    (
        A_avg_homoatomic_dist_by_shortest_dist,
        B_avg_homoatomic_dist_by_shortest_dist,
        C_avg_homoatomic_dist_by_shortest_dist,
        D_avg_homoatomic_dist_by_shortest_dist,
    ) = compute_avg_homoatomic_dist_by_site_shortest_dist(connections, A, B, C, D)
    (
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
    ) = get_A_and_B_and_C_and_D_count_in_best_label_per_element(connections, A, B, C, D)
    (
        A_avg_count_at_A_shorest_dist,
        A_avg_count_at_B_shorest_dist,
        A_avg_count_at_C_shorest_dist,
        A_avg_count_at_D_shorest_dist,
        B_avg_count_at_A_shorest_dist,
        B_avg_count_at_B_shorest_dist,
        B_avg_count_at_C_shorest_dist,
        B_avg_count_at_D_shorest_dist,
        C_avg_count_at_A_shorest_dist,
        C_avg_count_at_B_shorest_dist,
        C_avg_count_at_C_shorest_dist,
        C_avg_count_at_D_shorest_dist,
        D_avg_count_at_A_shorest_dist,
        D_avg_count_at_B_shorest_dist,
        D_avg_count_at_C_shorest_dist,
        D_avg_count_at_D_shorest_dist,
    ) = get_avg_A_and_B_and_C_and_D_count_in_per_element(connections, A, B, C, D)
    # 1. Compute the first, second shortest distances and count
    first_second_dist_per_site_data = count_first_second_min_dist(connections)
    # 2. Compute the best site for each label, determined by the shortest distance
    best_site_data = extract_best_labels(first_second_dist_per_site_data)
    # 3. Tol result
    tol_results = extract_shortest_dist_with_tol(best_site_data, connections)
    A_shortest_dist_count_within_tol = tol_results[A]["shortest_dist_count_within_tol"]
    B_shortest_dist_count_within_tol = tol_results[B]["shortest_dist_count_within_tol"]
    C_shortest_dist_count_within_tol = tol_results[C]["shortest_dist_count_within_tol"]
    D_shortest_dist_count_within_tol = tol_results[D]["shortest_dist_count_within_tol"]
    avg_tol_results = extract_avg_shortest_dist_with_tol(connections)
    A_avg_shortest_dist_within_tol_count = avg_tol_results[A]["avg_shortest_dist_within_tol_count"]
    B_avg_shortest_dist_within_tol_count = avg_tol_results[B]["avg_shortest_dist_within_tol_count"]
    C_avg_shortest_dist_within_tol_count = avg_tol_results[C]["avg_shortest_dist_within_tol_count"]
    D_avg_shortest_dist_within_tol_count = avg_tol_results[D]["avg_shortest_dist_within_tol_count"]
    A_best_label = best_site_data[A]["best_label"]
    B_best_label = best_site_data[B]["best_label"]
    C_best_label = best_site_data[C]["best_label"]
    D_best_label = best_site_data[D]["best_label"]
    (
        A_homoatomic_dist_by_shortest_dist,
        B_homoatomic_dist_by_shortest_dist,
        C_homoatomic_dist_by_shortest_dist,
        D_homoatomic_dist_by_shortest_dist,
    ) = compute_homoatomic_dist_by_site_shortest_dist(connections, A_best_label, B_best_label, C_best_label, D_best_label)
    # First shortest distance
    A_shortest_dist = best_site_data[A]["best_label_details"]["shortest_dist"]
    B_shortest_dist = best_site_data[B]["best_label_details"]["shortest_dist"]
    C_shortest_dist = best_site_data[C]["best_label_details"]["shortest_dist"]
    D_shortest_dist = best_site_data[D]["best_label_details"]["shortest_dist"]
    # Second shortest distance
    A_second_shortest_dist = best_site_data[A]["best_label_details"]["second_shortest_dist"]
    B_second_shortest_dist = best_site_data[B]["best_label_details"]["second_shortest_dist"]
    C_second_shortest_dist = best_site_data[C]["best_label_details"]["second_shortest_dist"]
    D_second_shortest_dist = best_site_data[D]["best_label_details"]["second_shortest_dist"]
    # First shortest distance count
    A_shortest_dist_count = best_site_data[A]["best_label_details"]["counts"][A_shortest_dist]
    B_shortest_dist_count = best_site_data[B]["best_label_details"]["counts"][B_shortest_dist]
    C_shortest_dist_count = best_site_data[C]["best_label_details"]["counts"][C_shortest_dist]
    D_shortest_dist_count = best_site_data[D]["best_label_details"]["counts"][D_shortest_dist]
    # Second shortest distance count
    A_second_shortest_dist_count = best_site_data[A]["best_label_details"]["counts"][A_second_shortest_dist]
    B_second_shortest_dist_count = best_site_data[B]["best_label_details"]["counts"][B_second_shortest_dist]
    C_second_shortest_dist_count = best_site_data[C]["best_label_details"]["counts"][C_second_shortest_dist]
    D_second_shortest_dist_count = best_site_data[D]["best_label_details"]["counts"][D_second_shortest_dist]
    # Avg shortest distance count across site labels per element
    A_avg_shortest_dist_count = best_site_data[A]["avg_shortest_dist"]
    B_avg_shortest_dist_count = best_site_data[B]["avg_shortest_dist"]
    C_avg_shortest_dist_count = best_site_data[C]["avg_shortest_dist"]
    D_avg_shortest_dist_count = best_site_data[D]["avg_shortest_dist"]
    # Avg second shortest distance count across site labels per element
    A_avg_second_shortest_dist_count = best_site_data[A]["avg_second_shortest_dist_count"]
    B_avg_second_shortest_dist_count = best_site_data[B]["avg_second_shortest_dist_count"]
    C_avg_second_shortest_dist_count = best_site_data[C]["avg_second_shortest_dist_count"]
    D_avg_second_shortest_dist_count = best_site_data[D]["avg_second_shortest_dist_count"]
    # Get avg second by first shortest distance ratio across site labels per element
    avg_second_by_first_dist = get_avg_second_by_first_shortest_dist_ratio(first_second_dist_per_site_data, connections)
    A_avg_second_by_first_shortest_dist = avg_second_by_first_dist[A]["avg_second_by_first_shortest_dist"]
    B_avg_second_by_first_shortest_dist = avg_second_by_first_dist[B]["avg_second_by_first_shortest_dist"]
    C_avg_second_by_first_shortest_dist = avg_second_by_first_dist[C]["avg_second_by_first_shortest_dist"]
    D_avg_second_by_first_shortest_dist = avg_second_by_first_dist[D]["avg_second_by_first_shortest_dist"]

    results = {
        # Shortest distance count
        "ENV_A_shortest_dist_count": A_shortest_dist_count,
        "ENV_B_shortest_dist_count": B_shortest_dist_count,
        "ENV_C_shortest_dist_count": C_shortest_dist_count,
        "ENV_D_shortest_dist_count": D_shortest_dist_count,
        # Avg shortest distance count
        "ENV_A_avg_shortest_dist_count": A_avg_shortest_dist_count,
        "ENV_B_avg_shortest_dist_count": B_avg_shortest_dist_count,
        "ENV_C_avg_shortest_dist_count": C_avg_shortest_dist_count,
        "ENV_D_avg_shortest_dist_count": D_avg_shortest_dist_count,
        # Shortest distance count within tolerance
        "ENV_A_shortest_tol_dist_count": A_shortest_dist_count_within_tol,
        "ENV_B_shortest_tol_dist_count": B_shortest_dist_count_within_tol,
        "ENV_C_shortest_tol_dist_count": C_shortest_dist_count_within_tol,
        "ENV_D_shortest_tol_dist_count": D_shortest_dist_count_within_tol,
        # Avg shortest distance count within tolerance
        "ENV_A_avg_shortest_dist_within_tol_count": A_avg_shortest_dist_within_tol_count,
        "ENV_B_avg_shortest_dist_within_tol_count": B_avg_shortest_dist_within_tol_count,
        "ENV_C_avg_shortest_dist_within_tol_count": C_avg_shortest_dist_within_tol_count,
        "ENV_D_avg_shortest_dist_within_tol_count": D_avg_shortest_dist_within_tol_count,
        # Second by first shortest distance ratio
        "ENV_A_second_by_first_shortest_dist": A_second_shortest_dist / A_shortest_dist,
        "ENV_B_second_by_first_shortest_dist": B_second_shortest_dist / B_shortest_dist,
        "ENV_C_second_by_first_shortest_dist": C_second_shortest_dist / C_shortest_dist,
        "ENV_D_second_by_first_shortest_dist": D_second_shortest_dist / D_shortest_dist,
        # Avg second by first shortest distance ratio
        "ENV_A_avg_second_by_first_shortest_dist": A_avg_second_by_first_shortest_dist,
        "ENV_B_avg_second_by_first_shortest_dist": B_avg_second_by_first_shortest_dist,
        "ENV_C_avg_second_by_first_shortest_dist": C_avg_second_by_first_shortest_dist,
        "ENV_D_avg_second_by_first_shortest_dist": D_avg_second_by_first_shortest_dist,
        # Second shortest distance count
        "ENV_A_second_shortest_dist_count": A_second_shortest_dist_count,
        "EnV_B_second_shortest_dist_count": B_second_shortest_dist_count,
        "ENV_C_second_shortest_dist_count": C_second_shortest_dist_count,
        "ENV_D_second_shortest_dist_count": D_second_shortest_dist_count,
        # Avg second shortest distance count
        "ENV_A_avg_second_shortest_dist_count": A_avg_second_shortest_dist_count,
        "ENV_B_avg_second_shortest_dist_count": B_avg_second_shortest_dist_count,
        "ENV_C_avg_second_shortest_dist_count": C_avg_second_shortest_dist_count,
        "ENV_D_avg_second_shortest_dist_count": D_avg_second_shortest_dist_count,
        # Homoatomic distance by shortest distance
        "ENV_A_homoatomic_dist_by_shortest_dist": A_homoatomic_dist_by_shortest_dist,
        "ENV_B_homoatomic_dist_by_shortest_dist": B_homoatomic_dist_by_shortest_dist,
        "ENV_C_homoatomic_dist_by_shortest_dist": C_homoatomic_dist_by_shortest_dist,
        "ENV_D_homoatomic_dist_by_shortest_dist": D_homoatomic_dist_by_shortest_dist,
        # Avg homoatomic distance by shortest distance
        "ENV_A_avg_homoatomic_dist_by_shortest_dist": A_avg_homoatomic_dist_by_shortest_dist,
        "ENV_B_avg_homoatomic_dist_by_shortest_dist": B_avg_homoatomic_dist_by_shortest_dist,
        "ENV_C_avg_homoatomic_dist_by_shortest_dist": C_avg_homoatomic_dist_by_shortest_dist,
        "ENV_D_avg_homoatomic_dist_by_shortest_dist": D_avg_homoatomic_dist_by_shortest_dist,
        # Count at shortest distance
        "ENV_A_count_at_A_shortest_dist": A_count_at_A_shortest_dist,
        "ENV_B_count_at_A_shortest_dist": B_count_at_A_shortest_dist,
        "ENV_C_count_at_A_shortest_dist": C_count_at_A_shortest_dist,
        "ENV_D_count_at_A_shortest_dist": D_count_at_A_shortest_dist,
        "ENV_A_avg_count_at_A_shortest_dist": A_avg_count_at_A_shorest_dist,
        "ENV_B_avg_count_at_A_shortest_dist": B_avg_count_at_A_shorest_dist,
        "ENV_C_avg_count_at_A_shortest_dist": C_avg_count_at_A_shorest_dist,
        "ENV_D_avg_count_at_A_shortest_dist": D_avg_count_at_A_shorest_dist,
        "ENV_A_count_at_B_shortest_dist": A_count_at_B_shortest_dist,
        "ENV_B_count_at_B_shortest_dist": B_count_at_B_shortest_dist,
        "ENV_C_count_at_B_shortest_dist": C_count_at_B_shortest_dist,
        "ENV_D_count_at_B_shortest_dist": D_count_at_B_shortest_dist,
        "ENV_A_avg_count_at_B_shortest_dist": A_avg_count_at_B_shorest_dist,
        "ENV_B_avg_count_at_B_shortest_dist": B_avg_count_at_B_shorest_dist,
        "ENV_C_avg_count_at_B_shortest_dist": C_avg_count_at_B_shorest_dist,
        "ENV_D_avg_count_at_B_shortest_dist": D_avg_count_at_B_shorest_dist,
        "ENV_A_count_at_C_shortest_dist": A_count_at_C_shortest_dist,
        "ENV_B_count_at_C_shortest_dist": B_count_at_C_shortest_dist,
        "ENV_C_count_at_C_shortest_dist": C_count_at_C_shortest_dist,
        "ENV_D_count_at_C_shortest_dist": D_count_at_C_shortest_dist,
        "ENV_A_avg_count_at_C_shortest_dist": A_avg_count_at_C_shorest_dist,
        "ENV_B_avg_count_at_C_shortest_dist": B_avg_count_at_C_shorest_dist,
        "ENV_C_avg_count_at_C_shortest_dist": C_avg_count_at_C_shorest_dist,
        "ENV_D_avg_count_at_C_shortest_dist": D_avg_count_at_C_shorest_dist,
        "ENV_A_count_at_D_shortest_dist": A_count_at_D_shortest_dist,
        "ENV_B_count_at_D_shortest_dist": B_count_at_D_shortest_dist,
        "ENV_C_count_at_D_shortest_dist": C_count_at_D_shortest_dist,
        "ENV_D_count_at_D_shortest_dist": D_count_at_D_shortest_dist,
        "ENV_A_avg_count_at_D_shortest_dist": A_avg_count_at_D_shorest_dist,
        "ENV_B_avg_count_at_D_shortest_dist": B_avg_count_at_D_shorest_dist,
        "ENV_C_avg_count_at_D_shortest_dist": C_avg_count_at_D_shorest_dist,
        "ENV_D_avg_count_at_D_shortest_dist": D_avg_count_at_D_shorest_dist,
    }
    return results
