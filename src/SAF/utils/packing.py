from cifkit import Cif
from numpy import cos, pi, sqrt


def compute_efficiency(
    cif: Cif,
    radius_dict,
) -> float:
    """Compute the packing efficiency of a crystal structure.

    It uses the number of multiplicities of atoms in the CIF loop values
    and the CIF radii dictionary to calculate the total volume occupied
    by the atoms, and then divides it by the volume of the unit cell.
    """
    elements = cif.unique_elements
    atom_counts = {element: 0 for element in elements}
    atom_site_types = cif._loop_values[1]
    atom_site_symmetry_multiplicities = cif._loop_values[2]
    # Calculate atom counts
    for (
        atom_site_type,
        atom_site_symmetry_multiplicity,
    ) in zip(atom_site_types, atom_site_symmetry_multiplicities):
        if atom_site_type in atom_counts:
            atom_counts[atom_site_type] += int(atom_site_symmetry_multiplicity)
    # Calculate total volume for all atom types
    vol_of_atoms = 0
    for atom, count in atom_counts.items():
        vol_of_atoms += count * (4 / 3) * pi * radius_dict[atom] ** 3
    vol_of_unt_cell = _get_unit_cell_volume(cif.unitcell_lengths, cif.unitcell_angles)
    packing_eff_refined = vol_of_atoms / vol_of_unt_cell
    return float(packing_eff_refined)


def _get_unit_cell_volume(lengths, angles):
    a_length, b_length, c_length = lengths
    alpha_angle, beta_angle, gamma_angle = angles

    volume = (
        a_length
        * b_length
        * c_length
        * sqrt(
            1
            - cos(alpha_angle) ** 2
            - cos(beta_angle) ** 2
            - cos(gamma_angle) ** 2
            + 2 * cos(alpha_angle) * cos(beta_angle) * cos(gamma_angle)
        )
    )
    return volume
