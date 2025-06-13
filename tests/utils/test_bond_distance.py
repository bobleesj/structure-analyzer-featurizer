import pytest
from core.utils.bond import get_min_distances_by_labels

# Sample bond distance data using Th (A), Os (B)
binary_sample_data = {
    ("Th", "Th"): 1.1,
    ("Os", "Os"): 1.2,
    ("Th", "Os"): 1.3,
}
def test_get_shortest_bond_distances_by_AB():
    result = get_min_distances_by_labels(binary_sample_data, ["Th", "Os"], labels=["A", "B"])
    expected = {
        "AA": 1.1,
        "BB": 1.2,
        "AB": 1.3,
    }
    assert result == expected

ternary_sample_data = {
    ("U", "U"): 1.0,
    ("U", "Rh"): 1.6,
    ("U", "In"): 1.7,
    ("Rh", "Rh"): 1.4,
    ("Rh", "In"): 1.8,
    ("In", "In"): 1.5,
}
def test_get_shortest_bond_distances_by_RMX():
    result = get_min_distances_by_labels(ternary_sample_data, ["U", "Rh", "In"], labels=["R", "M", "X"])
    expected = {
        "RR": 1.0,
        "RM": 1.6,
        "RX": 1.7,
        "MM": 1.4,
        "MX": 1.8,
        "XX": 1.5,
    }
    assert result == expected


# Sample quaternary bond distance data using Cu (A), U (B), Rh (C), In (D)
quaternary_sample_data = {
    ("Cu", "Cu"): 1.0,
    ("U", "U"): 1.1,
    ("Rh", "Rh"): 1.2,
    ("In", "In"): 1.3,
    ("Cu", "U"): 1.4,
    ("Cu", "Rh"): 1.5,
    ("Cu", "In"): 1.6,
    ("U", "Rh"): 1.7,
    ("U", "In"): 1.8,
    ("Rh", "In"): 1.9,
}

def test_get_shortest_bond_distances_by_quaternary():
    result = get_min_distances_by_labels(quaternary_sample_data, ["Cu", "U", "Rh", "In"], labels=["A", "B", "C", "D"])
    expected = {
        "AA": 1.0,
        "BB": 1.1,
        "CC": 1.2,
        "DD": 1.3,
        "AB": 1.4,
        "AC": 1.5,
        "AD": 1.6,
        "BC": 1.7,
        "BD": 1.8,
        "CD": 1.9,
    }
    assert result == expected