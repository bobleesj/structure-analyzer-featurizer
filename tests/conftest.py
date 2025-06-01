from cifkit import Cif
import pytest


@pytest.fixture
def cif_ThGe():
    return Cif("tests/data/ThGe.cif")
