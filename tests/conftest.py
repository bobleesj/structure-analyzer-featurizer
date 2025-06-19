import pytest
from cifkit import Cif

"""
Binary
"""

@pytest.fixture
def ThSb_cif():
    cif = Cif("tests/cif/binary/ThSb.cif", supercell_size=2)
    cif.compute_connections()
    return cif

@pytest.fixture
def Th7Rh3_cif():
    cif = Cif("tests/cif/binary/Th7Rh3.cif", supercell_size=2)
    cif.compute_connections()
    cif.compute_CN()
    return cif

@pytest.fixture
def Dy2Co17_cif():
    cif = Cif("tests/cif/binary/Dy2Co17.cif", supercell_size=2)
    cif.compute_connections()
    return cif


@pytest.fixture
def RhSb2_cif():
    cif = Cif("tests/cif/binary/RhSb2.cif", supercell_size=2)
    cif.compute_connections()
    cif.compute_CN()
    return cif

@pytest.fixture
def RhSb_elements_tuple():
    return ("Rh", "Sb")

@pytest.fixture
def ThRh_elements_tuple():
    return ("Th", "Rh")

@pytest.fixture
def ThSb_elements_tuple():
    return ("Th", "Sb")

"""
Ternary
"""


@pytest.fixture
def URhIn_cif():
    cif = Cif("tests/cif/ternary/URhIn.cif", supercell_size=2)
    cif.compute_connections()
    cif.compute_CN()
    return cif

@pytest.fixture
def URhIn_elements_tuple():
    return ("U", "Rh", "In")

"""
Quaternary
"""


@pytest.fixture
def Tb4RhInGe4_cif():
    # Tested that supercell size 2 or 3 both work
    cif = Cif("tests/cif/quaternary/Tb4RhInGe4.cif", supercell_size=2)
    cif.compute_connections()
    cif.compute_CN()
    return cif

@pytest.fixture
def TbRhInGe_elements_tuple():
    return ("Tb", "Rh", "In", "Ge")
