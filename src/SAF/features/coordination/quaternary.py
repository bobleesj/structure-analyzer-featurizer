from cifkit import Cif

from SAF.features.coordination.helper import get_CN_atom_count_data


def compute_features(cif: Cif, elements):
    avg_CN_metrics, avg_CN_atom_count = get_CN_atom_count_data(cif, elements)
    return {
        "CN_AVG_coordination_number": avg_CN_metrics["avg"]["number_of_vertices"],
        "CN_AVG_A_atom_count": avg_CN_atom_count["avg"]["A_count"],
        "CN_AVG_B_atom_count": avg_CN_atom_count["avg"]["B_count"],
        "CN_AVG_C_atom_count": avg_CN_atom_count["avg"]["C_count"],
        "CN_AVG_D_atom_count": avg_CN_atom_count["avg"]["D_count"],
        "CN_AVG_polyhedron_volume": avg_CN_metrics["avg"]["volume_of_polyhedron"],
        "CN_AVG_central_atom_to_center_of_mass_dist": avg_CN_metrics["avg"]["distance_from_avg_point_to_center"],
        "CN_AVG_number_of_edges": avg_CN_metrics["avg"]["number_of_edges"],
        "CN_AVG_number_of_faces": avg_CN_metrics["avg"]["number_of_faces"],
        "CN_AVG_shortest_distance_to_face": avg_CN_metrics["avg"]["shortest_distance_to_face"],
        "CN_AVG_shortest_distance_to_edge": avg_CN_metrics["avg"]["shortest_distance_to_edge"],
        "CN_AVG_volume_of_inscribed_sphere": avg_CN_metrics["avg"]["volume_of_inscribed_sphere"],
        "CN_AVG_packing_efficiency": avg_CN_metrics["avg"]["packing_efficiency"],
        "CN_MIN_coordination_number": avg_CN_metrics["min"]["number_of_vertices"],
        "CN_MIN_A_atom_count": avg_CN_atom_count["min"]["A_count"],
        "CN_MIN_B_atom_count": avg_CN_atom_count["min"]["B_count"],
        "CN_MIN_C_atom_count": avg_CN_atom_count["min"]["C_count"],
        "CN_MIN_D_atom_count": avg_CN_atom_count["min"]["D_count"],
        "CN_MIN_polyhedron_volume": avg_CN_metrics["min"]["volume_of_polyhedron"],
        "CN_MIN_central_atom_to_center_of_mass_dist": avg_CN_metrics["min"]["distance_from_avg_point_to_center"],
        "CN_MIN_number_of_edges": avg_CN_metrics["min"]["number_of_edges"],
        "CN_MIN_number_of_faces": avg_CN_metrics["min"]["number_of_faces"],
        "CN_MIN_shortest_distance_to_face": avg_CN_metrics["min"]["shortest_distance_to_face"],
        "CN_MIN_shortest_distance_to_edge": avg_CN_metrics["min"]["shortest_distance_to_edge"],
        "CN_MIN_volume_of_inscribed_sphere": avg_CN_metrics["min"]["volume_of_inscribed_sphere"],
        "CN_MIN_packing_efficiency": avg_CN_metrics["min"]["packing_efficiency"],
        "CN_MAX_coordination_number": avg_CN_metrics["max"]["number_of_vertices"],
        "CN_MAX_A_atom_count": avg_CN_atom_count["max"]["A_count"],
        "CN_MAX_B_atom_count": avg_CN_atom_count["max"]["B_count"],
        "CN_MAX_C_atom_count": avg_CN_atom_count["max"]["C_count"],
        "CN_MAX_D_atom_count": avg_CN_atom_count["max"]["D_count"],
        "CN_MAX_polyhedron_volume": avg_CN_metrics["max"]["volume_of_polyhedron"],
        "CN_MAX_central_atom_to_center_of_mass_dist": avg_CN_metrics["max"]["distance_from_avg_point_to_center"],
        "CN_MAX_number_of_edges": avg_CN_metrics["max"]["number_of_edges"],
        "CN_MAX_number_of_faces": avg_CN_metrics["max"]["number_of_faces"],
        "CN_MAX_shortest_distance_to_face": avg_CN_metrics["max"]["shortest_distance_to_face"],
        "CN_MAX_shortest_distance_to_edge": avg_CN_metrics["max"]["shortest_distance_to_edge"],
        "CN_MAX_volume_of_inscribed_sphere": avg_CN_metrics["max"]["volume_of_inscribed_sphere"],
        "CN_MAX_packing_efficiency": avg_CN_metrics["max"]["packing_efficiency"],
    }
