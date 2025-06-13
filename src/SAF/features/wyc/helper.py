from cifkit.utils.string_parser import strip_numbers_and_symbols


def parse_site_data(loop_values):
    # Initialize a dictionary to store element information
    data = {}
    # Get the number of atoms
    num_site_labels = len(loop_values[0])
    # Loop over all atoms
    for i in range(num_site_labels):
        # Get atomic info
        site_label = loop_values[0][i]
        element = strip_numbers_and_symbols(loop_values[1][i])
        multiplicity = int(loop_values[2][i])
        if element not in data:
            data[element] = {
                "sites": 0,
                "multiplicity": 0,
                "lowest_wyckoff_multiplicity": multiplicity,
                "lowest_wyckoff_element": site_label,
            }
        # Update the atom information in the dictionary
        data[element]["sites"] += 1
        data[element]["multiplicity"] += multiplicity
        # Update the element with the lowest Wyckoff multiplicity
        if multiplicity < data[element]["multiplicity"]:
            data[element]["lowest_wyckoff_multiplicity"] = multiplicity
            data[element]["lowest_wyckoff_element"] = site_label
    return data


def get_binary_site_info(loop_values, A, B):
    atomic_env = parse_site_data(loop_values)
    A_env, B_env = None, None
    # Check if the desired elements are present
    if A in atomic_env:
        A_env = atomic_env[A]
    if B in atomic_env:
        B_env = atomic_env[B]
    return A_env, B_env


def get_ternary_site_info(loop_values, R, M, X):
    atomic_env = parse_site_data(loop_values)
    R_env, M_env, X_env = None, None, None
    # Check if the desired elements are present
    if R in atomic_env:
        R_env = atomic_env[R]
    if M in atomic_env:
        M_env = atomic_env[M]
    if X in atomic_env:
        X_env = atomic_env[X]
    return R_env, M_env, X_env
