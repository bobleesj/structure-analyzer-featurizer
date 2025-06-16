import itertools

from SAF.config import get_labels


def get_binary_AB_elements(elements: list[str]) -> tuple[str, str]:
    """Get A, B elements from a list of two elements using label
    groups."""
    if len(elements) != 2:
        raise ValueError("Input must be a list of exactly two elements.")

    labels = get_labels()[2]
    A_labels = labels["A"]
    B_labels = labels["B"]

    e0, e1 = elements

    if e0 in A_labels and e1 in B_labels:
        return e0, e1
    elif e1 in A_labels and e0 in B_labels:
        return e1, e0
    else:
        return tuple(sorted(elements))


def get_ternary_RMX_elements(elements: list[str]) -> tuple[str, str, str]:
    """Get R, M, X elements from a list of three elements using label
    groups."""
    if len(elements) != 3:
        raise ValueError("Input must be a list of exactly three elements.")

    labels = get_labels()[3]
    R_labels = labels["R"]
    M_labels = labels["M"]
    X_labels = labels["X"]
    for perm in itertools.permutations(elements):
        if perm[0] in R_labels and perm[1] in M_labels and perm[2] in X_labels:
            return perm
    raise ValueError(f"Could not determine R, M, X ordering for elements: {elements}")


def get_quaternary_ABCD_elements(elements: list[str]) -> tuple[str, str, str, str]:
    """Get A, B, C, D elements from a list of four elements using label
    groups."""
    if len(elements) != 4:
        raise ValueError("Input must be a list of exactly four elements.")

    labels = get_labels()[4]
    A_labels = labels["A"]
    B_labels = labels["B"]
    C_labels = labels["C"]
    D_labels = labels["D"]

    for perm in itertools.permutations(elements):
        if perm[0] in A_labels and perm[1] in B_labels and perm[2] in C_labels and perm[3] in D_labels:
            return perm
    raise ValueError(f"Could not determine A, B, C, D ordering for elements: {elements}")
