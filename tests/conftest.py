import pytest
from cifkit import Cif


@pytest.fixture
def cif_ThGe():
    return Cif("tests/data/ThGe.cif")
