import pytest
from cifkit import Cif

"""
Binary
"""


@pytest.fixture(scope="module")
def ThSb_cif():
    cif = Cif("tests/cif/binary/ThSb.cif")
    cif.compute_connections()
    return cif


@pytest.fixture(scope="module")
def Dy2Co17_cif():
    cif = Cif("tests/cif/binary/Dy2Co17.cif", supercell_size=2)
    cif.compute_connections()
    return cif


@pytest.fixture(scope="module")
def RhSb2_cif():
    cif = Cif("tests/cif/binary/RhSb2.cif")
    cif.compute_connections()
    return cif


@pytest.fixture(scope="module")
def Th7Rh3_cif():
    cif = Cif("tests/cif/binary/Th7Rh3.cif")
    cif.compute_connections()
    return cif


@pytest.fixture(scope="module")
def URhIn_cif():
    cif = Cif("tests/cif/ternary/URhIn.cif")
    cif.compute_connections()
    return cif


@pytest.fixture(scope="module")
def Tb4RhInGe4_cif():
    cif = Cif("tests/cif/quaternary/Tb4RhInGe4.cif", supercell_size=3)
    cif.compute_connections()
    return cif


# @pytest.fixture(scope="module")
# def Th7Rh3_cif():
#     cif = Cif("tests/cif/binary/Th7Rh3.cif")
#     cif.compute_connections()
#     return cif