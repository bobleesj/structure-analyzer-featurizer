from cifkit import Cif
from cifkit.data import radius_optimization as radius_opt
from SAF.utils import bond, element_order, packing
from SAF.features.interatomic import helper


def compute_features(cif: Cif):
    elements = list(cif.unique_elements)
    A, B, C, D = element_order.get_quaternary_ABCD_elements(elements)
    A_CIF_rad = cif.radius_values[A]["CIF_radius"]
    B_CIF_rad = cif.radius_values[B]["CIF_radius"]
    C_CIF_rad = cif.radius_values[C]["CIF_radius"]
    D_CIF_rad = cif.radius_values[D]["CIF_radius"]
    CIF_rad_refined, obj_value = radius_opt.get_refined_CIF_radius([A, B, C, D], cif.shortest_bond_pair_distance, elements_ordered=False)
    A_CIF_rad_refined = CIF_rad_refined[A]
    B_CIF_rad_refined = CIF_rad_refined[B]
    C_CIF_rad_refined = CIF_rad_refined[C]
    D_CIF_rad_refined = CIF_rad_refined[D]
    min_bond_dists = bond.get_min_distances_by_labels(cif.shortest_bond_pair_distance, [A, B, C, D], labels=["A", "B", "C", "D"])
    distAA = min_bond_dists["AA"]
    distAB = min_bond_dists["AB"]
    distAC = min_bond_dists["AC"]
    distAD = min_bond_dists["AD"]
    distBB = min_bond_dists["BB"]
    distBC = min_bond_dists["BC"]
    distBD = min_bond_dists["BD"]
    distCC = min_bond_dists["CC"]    
    distCD = min_bond_dists["CD"]
    distDD = min_bond_dists["DD"]
    
    # Distances    
    data = {
        "Entry": cif.file_name_without_ext,
        "Formula": cif.formula,
        "Structure": cif.structure,
        "A": A,
        "B": B,
        "C": C,
        "D": D,
        "INT_distAA": distAA,
        "INT_distBB": distBB,
        "INT_distCC": distCC,
        "INT_distDD": distDD,
        "INT_distAB": distAB,
        "INT_distAC": distAC,
        "INT_distAD": distAD,
        "INT_distBC": distBC,
        "INT_distBD": distBD,
        "INT_distCD": distCD,
        "INT_Asize": A_CIF_rad,
        "INT_Bsize": B_CIF_rad,
        "INT_Csize": C_CIF_rad,
        "INT_Dsize": D_CIF_rad,
        "INT_Asize_ref": A_CIF_rad_refined,
        "INT_Bsize_ref": B_CIF_rad_refined,
        "INT_Csize_ref": C_CIF_rad_refined,
        "INT_Dsize_ref": D_CIF_rad_refined,
        "INT_R_factor": obj_value
    }
    

    return data