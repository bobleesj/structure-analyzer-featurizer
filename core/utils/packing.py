from numpy import cos, pi, sqrt


def compute_packing_efficiency(
    atoms,
    CIF_loop_values,
    radius_dict,
    cell_lengths,
    cell_angles_rad,
):
    """Compute the packing efficiency of a crystal structure.

    It usees the number of multiplicities of atoms in the CIF loop
    values and the CIF radii dictionary to calculate the total volume
    occupied by the atoms, and then divides it by the volume of the unit
    cell.
    """
    atom_counts = {atom: 0 for atom in atoms}
    atom_site_types = CIF_loop_values[1]
    atom_site_symmetry_multiplicities = CIF_loop_values[2]
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
    vol_of_unt_cell = _get_unit_cell_volume(cell_lengths, cell_angles_rad)
    packing_eff_refined = vol_of_atoms / vol_of_unt_cell

    return round(packing_eff_refined, 5)


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
