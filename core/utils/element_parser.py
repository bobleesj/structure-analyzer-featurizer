import itertools

from core.config import get_binary_AB_labels, get_ternary_RMX_labels


def get_binary_AB_elements(
    elements: list[str],
) -> tuple[str, str]:
    """Get A, B elements from a list of two elements."""
    A_labels, B_labels = get_binary_AB_labels()
    A: str = None
    B: str = None
    if elements[0] in A_labels and elements[1] in B_labels:
        A = elements[0]
        B = elements[1]
    elif elements[0] in B_labels and elements[1] in A_labels:
        A = elements[1]
        B = elements[0]
    else:
        return sorted(elements)
    return A, B


def get_ternary_RMX_elements(elements: list[str]) -> tuple[str, str, str]:
    """Get R, M, X elements from a list of three elements based on RMX label
    groups."""

    if len(elements) != 3:
        raise ValueError("Input must be a list of exactly three elements.")

    R_labels, M_labels, X_labels = get_ternary_RMX_labels()

    for perm in itertools.permutations(elements):
        if perm[0] in R_labels and perm[1] in M_labels and perm[2] in X_labels:
            return perm  # Found valid R, M, X ordering

    raise ValueError(f"Could not determine RMX ordering for elements: {elements}")
