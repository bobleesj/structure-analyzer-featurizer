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
def Th7Rh3_cif():
    cif = Cif("tests/cif/binary/Th7Rh3.cif", supercell_size=2)
    cif.compute_connections()
    cif.compute_CN()
    return cif


"""
Ternary
"""


@pytest.fixture
def URhIn_cif():
    cif = Cif("tests/cif/ternary/URhIn.cif", supercell_size=2)
    cif.compute_connections()
    cif.compute_CN()
    return cif


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
