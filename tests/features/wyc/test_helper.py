from cifkit import Cif
from SAF.features.wyc.helper import (
    get_binary_site_info,
    get_ternary_site_info,
    _parse_site_data,
)


def test__parse_site_data():
    file_path = "tests/cif/binary/Th7Rh3.cif"
    cif = Cif(file_path)
    atomic_env = _parse_site_data(cif._loop_values)

    assert atomic_env == {
        "Rh": {
            "sites": 1,
            "multiplicity": 6,
            "lowest_wyckoff_multiplicity": 6,
            "lowest_wyckoff_element": "Rh1",
        },
        "Th": {
            "sites": 3,
            "multiplicity": 14,
            "lowest_wyckoff_multiplicity": 2,
            "lowest_wyckoff_element": "Th3",
        },
    }


def test_get_binary_site_info():
    file_path = "tests/cif/binary/Th7Rh3.cif"
    cif = Cif(file_path)
    A_info, B_info = get_binary_site_info(cif._loop_values, "Th", "Rh")

    assert A_info == {
        "sites": 3,
        "multiplicity": 14,
        "lowest_wyckoff_multiplicity": 2,
        "lowest_wyckoff_element": "Th3",
    }
    assert B_info == {
        "sites": 1,
        "multiplicity": 6,
        "lowest_wyckoff_multiplicity": 6,
        "lowest_wyckoff_element": "Rh1",
    }


def test_get_ternary_site_info():
    file_path = "tests/cif/ternary/URhIn.cif"
    cif = Cif(file_path)
    R_env, M_env, X_env = get_ternary_site_info(cif._loop_values, "U", "Rh", "In")

    assert R_env == {
        "sites": 1,
        "multiplicity": 3,
        "lowest_wyckoff_multiplicity": 3,
        "lowest_wyckoff_element": "U1",
    }
    assert M_env == {
        "sites": 2,
        "multiplicity": 3,
        "lowest_wyckoff_multiplicity": 1,
        "lowest_wyckoff_element": "Rh2",
    }

    assert X_env == {
        "sites": 1,
        "multiplicity": 3,
        "lowest_wyckoff_multiplicity": 3,
        "lowest_wyckoff_element": "In1",
    }
