def get_binary_AB_labels() -> tuple[list[str], list[str]]:
    A_labels = [
        "Si",
        "Sc",
        "Fe",
        "Co",
        "Ni",
        "Ga",
        "Ge",
        "Y",
        "Ru",
        "Rh",
        "Pd",
        "In",
        "Sn",
        "Sb",
        "La",
        "Ce",
        "Pr",
        "Nd",
        "Sm",
        "Eu",
        "Gd",
        "Tb",
        "Dy",
        "Ho",
        "Er",
        "Tm",
        "Yb",
        "Lu",
        "Os",
    ]
    B_labels = [
        "Ir",
        "Pt",
        "Th",
        "U",
        "Al",
        "Mo",
        "Hf",
        "Ta",
        "Ag",
        "As",
        "Au",
        "B",
        "Ba",
        "Be",
        "Bi",
        "C",
        "Ca",
        "Cd",
        "Cr",
        "Cs",
        "Cu",
        "Hg",
        "K",
        "Li",
        "Mg",
        "Mn",
        "Na",
        "Nb",
        "P",
        "Pb",
        "Rb",
        "Re",
        "S",
        "Se",
        "Sr",
        "Te",
        "Ti",
        "Tl",
        "V",
        "W",
        "Zn",
        "Zr",
    ]

    return A_labels, B_labels


def get_ternary_RMX_labels() -> tuple[list[str], list[str], list[str]]:
    R_labels = [
        "Si",
        "Sc",
        "Fe",
        "Co",
        "Ni",
        "Ga",
        "Ge",
        "Y",
        "Ru",
        "Rh",
        "Pd",
        "In",
        "Sn",
        "Sb",
        "La",
        "Ce",
        "Pr",
        "Nd",
        "Sm",
        "Eu",
        "Gd",
        "Tb",
        "Dy",
    ]
    M_labels = [
        "Ho",
        "Er",
        "Tm",
        "Yb",
        "Lu",
        "Os",
        "Ir",
        "Pt",
        "Th",
        "U",
        "Al",
        "Mo",
        "Hf",
        "Ta",
        "Ag",
        "As",
        "Au",
        "B",
        "Ba",
        "Be",
        "Bi",
        "C",
    ]

    X_labels = [
        "Ca",
        "Cd",
        "Cr",
        "Cs",
        "Cu",
        "Hg",
        "K",
        "Li",
        "Mg",
        "Mn",
        "Na",
        "Nb",
        "P",
        "Pb",
        "Rb",
        "Re",
        "S",
        "Se",
        "Sr",
        "Te",
        "Ti",
        "Tl",
        "V",
        "W",
        "Zn",
        "Zr",
    ]

    return R_labels, M_labels, X_labels


def get_all_possible_elements() -> list[str]:
    possible_elements = [
        "Si",
        "Sc",
        "Fe",
        "Co",
        "Ni",
        "Ga",
        "Ge",
        "Y",
        "Ru",
        "Rh",
        "Pd",
        "In",
        "Sn",
        "Sb",
        "La",
        "Ce",
        "Pr",
        "Nd",
        "Sm",
        "Eu",
        "Gd",
        "Tb",
        "Dy",
        "Ho",
        "Er",
        "Tm",
        "Yb",
        "Lu",
        "Os",
        "Ir",
        "Pt",
        "Th",
        "U",
        "Al",
        "Mo",
        "Hf",
        "Ta",
        "Ag",
        "As",
        "Au",
        "B",
        "Ba",
        "Be",
        "Bi",
        "C",
        "Ca",
        "Cd",
        "Cr",
        "Cs",
        "Cu",
        "Hg",
        "K",
        "Li",
        "Mg",
        "Mn",
        "Na",
        "Nb",
        "P",
        "Pb",
        "Rb",
        "Re",
        "S",
        "Se",
        "Sr",
        "Te",
        "Ti",
        "Tl",
        "V",
        "W",
        "Zn",
        "Zr",
    ]
    return possible_elements
