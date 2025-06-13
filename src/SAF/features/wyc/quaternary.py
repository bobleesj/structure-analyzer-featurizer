from cifkit import Cif

from SAF.features.wyc import helper
from SAF.utils import element_order


def compute_features(cif: Cif):
    elements = list(cif.unique_elements)
    A, B, C, D = element_order.get_quaternary_ABCD_elements(elements)
    A_env, B_env, C_env, D_env = helper.get_quaternary_site_info(cif._loop_values, A, B, C, D)
    A_sites_total = A_env["sites"]
    B_sites_total = B_env["sites"]
    C_sites_total = C_env["sites"]
    D_sites_total = D_env["sites"]
    A_multiplicity_total = A_env["multiplicity"]
    B_multiplicity_total = B_env["multiplicity"]
    C_multiplicity_total = C_env["multiplicity"]
    D_multiplicity_total = D_env["multiplicity"]
    A_lowest_wyckoff_multiplicity = A_env["lowest_wyckoff_multiplicity"]
    B_lowest_wyckoff_multiplicity = B_env["lowest_wyckoff_multiplicity"]
    C_lowest_wyckoff_multiplicity = C_env["lowest_wyckoff_multiplicity"]
    D_lowest_wyckoff_multiplicity = D_env["lowest_wyckoff_multiplicity"]
    # Determine the lowest Wyckoff multiplicity
    min_wyckoff_multiplicity = min(
        A_lowest_wyckoff_multiplicity,
        B_lowest_wyckoff_multiplicity,
        C_lowest_wyckoff_multiplicity,
        D_lowest_wyckoff_multiplicity,
    )
    # Identify elements with the lowest Wyckoff multiplicity
    lowest_wyckoff_elements = []
    if A_lowest_wyckoff_multiplicity == min_wyckoff_multiplicity:
        lowest_wyckoff_elements.append(A)
    if B_lowest_wyckoff_multiplicity == min_wyckoff_multiplicity:
        lowest_wyckoff_elements.append(B)
    if C_lowest_wyckoff_multiplicity == min_wyckoff_multiplicity:
        lowest_wyckoff_elements.append(C)
    if D_lowest_wyckoff_multiplicity == min_wyckoff_multiplicity:
        lowest_wyckoff_elements.append(D)
    identical_lowest_wyckoff_multiplicity_count = len(lowest_wyckoff_elements)
    data = {
        "WYK_A_lowest_wyckoff": A_lowest_wyckoff_multiplicity,
        "WYK_B_lowest_wyckoff": B_lowest_wyckoff_multiplicity,
        "WYK_C_lowest_wyckoff": C_lowest_wyckoff_multiplicity,
        "WYK_D_lowest_wyckoff": D_lowest_wyckoff_multiplicity,
        "WYK_identical_lowest_wyckoff_count": identical_lowest_wyckoff_multiplicity_count,
        "WYK_A_sites_total": A_sites_total,
        "WYK_B_sites_total": B_sites_total,
        "WYK_C_sites_total": C_sites_total,
        "WYK_D_sites_total": D_sites_total,
        "WYK_A_multiplicity_total": A_multiplicity_total,
        "WYK_B_multiplicity_total": B_multiplicity_total,
        "WYK_C_multiplicity_total": C_multiplicity_total,
        "WYK_D_multiplicity_total": D_multiplicity_total,
    }
    uni_data = {
        "UNI_WYK_lowest_wyckoff": min_wyckoff_multiplicity,
    }
    return data, uni_data
