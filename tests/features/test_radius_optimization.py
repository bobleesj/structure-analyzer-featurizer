import pytest
from cifkit.data import radius_optimization as radius_opt
from core.utils import bond, element_order, packing


def test_binary_DyCo_cif(Dy2Co17_cif):
    # All expected values are from Oliynyk's video
    A = "Dy"
    B = "Co"
    # We want to find the refined radius based on the specific order of A, B instead
    # of the alphabetical order that is done by default when Dy2Co17 is initialized.
    assert Dy2Co17_cif.shortest_bond_pair_distance == {("Co", "Co"): 2.363, ("Co", "Dy"): 2.782, ("Dy", "Dy"): 4.06}
    refined_radius_dict, obj_value = radius_opt.get_refined_CIF_radius(
        [A, B], Dy2Co17_cif.shortest_bond_pair_distance, elements_ordered=False
    )
    assert refined_radius_dict[A] == pytest.approx(1.6062119417614027, abs=1e-4)
    assert refined_radius_dict[B] == pytest.approx(1.1757880582385976, abs=1e-4)
    assert obj_value == pytest.approx(0.010480551024582448, abs=1e-4)
    assert (refined_radius_dict[A] + refined_radius_dict[B]) == pytest.approx(2.782, abs=1e-4)
    packing_efficiency = packing.compute_efficiency(
        (A, B),
        Dy2Co17_cif._loop_values,
        refined_radius_dict,
        Dy2Co17_cif.unitcell_lengths,
        Dy2Co17_cif.unitcell_angles,
    )
    assert packing_efficiency == pytest.approx(0.61437, abs=1e-4)


def test_unit_cell_volume(Dy2Co17_cif):
    lenghts = Dy2Co17_cif.unitcell_lengths
    angles = Dy2Co17_cif.unitcell_angles
    volume = packing._get_unit_cell_volume(lenghts, angles)
    assert volume == pytest.approx(734.7396088113346, abs=1e-4)
