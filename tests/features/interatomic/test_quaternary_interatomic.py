import pytest
from core.features.interatomic.quaternary import (
    compute_features,
)


@pytest.mark.now
def test_binary_test(Tb4RhInGe4_cif):
    actual = compute_features(Tb4RhInGe4_cif)
    expected = {'Entry': 'Tb4RhInGe4', 'Formula': 'Tb4RhInGe4', 'Structure': 'Tb4RhInGe4', 'A': 'Tb', 'B': 'Rh', 'C': 'In', 'D': 'Ge', 'INT_distAA': 3.538, 'INT_distBB': 3.148, 'INT_distCC': 4.264, 'INT_distDD': 2.596, 'INT_distAB': 3.076, 'INT_distAC': 3.367, 'INT_distAD': 2.917, 'INT_distBC': 4.711, 'INT_distBD': 2.47, 'INT_distCD': 2.818, 'INT_Asize': 1.764, 'INT_Bsize': 1.345, 'INT_Csize': 1.624, 'INT_Dsize': 1.225, 'INT_Asize_ref': 0.7769957523126911, 'INT_Bsize_ref': 2.2990042476873094, 'INT_Csize_ref': 2.411995752312691, 'INT_Dsize_ref': 0.40600424768730903}
    print(actual)
    
    assert False

    for key, expected_value in expected.items():
        # For float
        if isinstance(expected_value, float):
            assert actual[key] == pytest.approx(expected_value, abs=0.001)
        # For str, integer, etc.
        else:
            assert actual[key] == expected_value
