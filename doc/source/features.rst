
Features
========

Binary
------

.. list-table::
  :header-rows: 1
  :widths: 5 30 65

  * - #
    - Feature
    - Description
  * - 1
    - Entry
    - Used to match with CAF data or any other data to merge in one single file
  * - 2
    - formula
    - Label
  * - 3
    - A
    - Element A matched with the group
  * - 4
    - B
    - Element B matched with the group
  * - 5
    - INT_AA_dist
    - Interatomic distances from CIF
  * - 6
    - INT_BB_dist
    - Interatomic distances from CIF
  * - 7
    - INT_AB_dist
    - Interatomic distances from CIF
  * - 8
    - INT_Asize
    - CIF radius for atom A
  * - 9
    - INT_Bsize
    - CIF radius for atom B
  * - 10
    - INT_Asize_by_Bsize
    - Radius ratio (CIF radius)
  * - 11
    - INT_AA_dist_by_2_by_Asize
    - Default size scale fit
  * - 12
    - INT_BB_dist_by_2_by_Bsize
    - Default size scale fit
  * - 13
    - INT_AB_dist_by_ABsizes
    - Default size scale
  * - 14
    - INT_Asize_ref
    - Refined radius
  * - 15
    - INT_Bsize_ref
    - Refined radius
  * - 16
    - INT_percent_diff_A_by_100
    - How much different from default scale
  * - 17
    - INT_percent_diff_B_by_100
    - How much different from default scale
  * - 18
    - INT_AA_dist_minus_ref_diff
    - Refined scale fitness (0 means the distance used for refinements)
  * - 19
    - INT_BB_dist_minus_ref_diff
    - Refined scale fitness (0 means the distance used for refinements)
  * - 20
    - INT_AB_dist_minus_ref_diff
    - Refined scale fitness (0 means the distance used for refinements)
  * - 21
    - INT_R_factor
    - R factor for the refinement (least square difference)
  * - 22
    - INT_UNI_shortest_homoatomic_dist
    - Shortest homoatomic distance
  * - 23
    - INT_UNI_shortest_heteroatomic_dist
    - Shortest heteroatomic distance
  * - 24
    - INT_UNI_shortest_homoatomic_dist_by_2_by_atom_size
    - Shortest homoatomic distance by 2 by atom size
  * - 25
    - INT_UNI_shortest_heteroatomic_dist_by_sum_of_atom_sizes
    - Shortest heteroatomic distance by sum of atom sizes
  * - 26
    - INT_UNI_shortest_homoatomic_dist_by_2_by_refined_atom_size
    - Shortest homoatomic distance by 2 by refined atom size
  * - 27
    - INT_UNI_shortest_heteroatomic_dist_by_sum_of_refined_atom_sizes
    - Shortest heteroatomic distance by sum of refined sizes
  * - 28
    - INT_UNI_highest_refined_percent_diff_abs
    - Highest refined percent difference by 100 (abs value)
  * - 29
    - INT_UNI_lowest_refined_percent_diff_abs
    - Lowest refined percent difference by 100 (abs value)
  * - 30
    - INT_UNI_packing_efficiency
    - Packing efficiency in unit cell with refined radius
  * - 31
    - WYC_A_lowest_wyckoff_label
    - Lowest Wyckoff number for element A
  * - 32
    - WYC_B_lowest_wyckoff_label
    - Lowest Wyckoff number for element B
  * - 33
    - WYC_identical_lowest_wyckoff_count
    - Number of sites with the lowest Wyckoff number
  * - 34
    - WYC_A_sites_total
    - Number of crystallographic sites for element A
  * - 35
    - WYC_B_sites_total
    - Number of crystallographic sites for element B
  * - 36
    - WYC_A_multiplicity_total
    - Sum of Wyckoff numbers for element A
  * - 37
    - WYC_B_multiplicity_total
    - Sum of Wyckoff numbers for element B
  * - 38
    - ENV_A_shortest_dist_count
    - Number of atoms that are at the shortest distance from atom A
  * - 39
    - ENV_B_shortest_dist_count
    - Number of atoms that are at the shortest distance from atom B
  * - 40
    - ENV_A_avg_shortest_dist_count
    - Average number of atoms that are at the shortest distance from atom A (case if multiple sites present)
  * - 41
    - ENV_B_avg_shortest_dist_count
    - Average number of atoms that are at the shortest distance from atom B (case if multiple sites present)
  * - 42
    - ENV_A_shortest_tol_dist_count
    - Number of atoms that are at the shortest distance from atom A (with some distance tolerance applied, default 5%)
  * - 43
    - ENV_B_shortest_tol_dist_count
    - Number of atoms that are at the shortest distance from atom B (with some distance tolerance applied, default 5%)
  * - 44
    - ENV_A_avg_shortest_dist_within_tol_count
    - Average number of atoms that are at the shortest distance from atom A (case if multiple sites present, with some distance tolerance applied, default 5%)
  * - 45
    - ENV_B_avg_shortest_dist_within_tol_count
    - Average number of atoms that are at the shortest distance from atom B (case if multiple sites present, with some distance tolerance applied, default 5%)
  * - 46
    - ENV_A_second_by_first_shortest_dist
    - 2nd shortest distance/1st shorted distance for atom A, measures distortion of polyhedron
  * - 47
    - ENV_B_second_by_first_shortest_dist
    - 2nd shortest distance/1st shorted distance for atom B, measures distortion of polyhedron
  * - 48
    - ENV_A_avg_second_by_first_shortest_dist
    - 2nd shortest distance/1st shorted distance for atom A, measures distortion of polyhedron (case if multiple sites present)
  * - 49
    - ENV_B_avg_second_by_first_shortest_dist
    - 2nd shortest distance/1st shorted distance for atom B, measures distortion of polyhedron (case if multiple sites present)
  * - 50
    - ENV_A_second_shortest_dist_count
    - 2nd shortest distance count for atom A
  * - 51
    - ENV_B_second_shortest_dist_count
    - 2nd shortest distance count for atom B
  * - 52
    - ENV_A_avg_second_shortest_dist_count
    - Average 2nd shortest distance count for atom A
  * - 53
    - ENV_B_avg_second_shortest_dist_count
    - Average 2nd shortest distance count for atom B
  * - 54
    - ENV_A_homoatomic_dist_by_shortest_dist
    - A-A distance / shortest distance
  * - 55
    - ENV_B_homoatomic_dist_by_shortest_dist
    - B-B distance / shortest distance
  * - 56
    - ENV_A_avg_homoatomic_dist_by_shortest_dist
    - Average A-A distance / shortest distance
  * - 57
    - ENV_B_avg_homoatomic_dist_by_shortest_dist
    - Average B-B distance / shortest distance
  * - 58
    - ENV_A_count_at_A_shortest_dist
    - Number of A atoms next to the A atoms at the shortest distance
  * - 59
    - ENV_A_count_at_B_shortest_dist
    - Number of A atoms next to the B atoms at the shortest distance
  * - 60
    - ENV_A_avg_count_at_A_shortest_dist
    - Average number of A atoms next to the A atoms at the shortest distance
  * - 61
    - ENV_A_avg_count_at_B_shortest_dist
    - Average number of A atoms next to the B atoms at the shortest distance
  * - 62
    - ENV_B_count_at_A_shortest_dist
    - Number of B atoms next to the A atoms at the shortest distance
  * - 63
    - ENV_B_count_at_B_shortest_dist
    - Number of B atoms next to the B atoms at the shortest distance
  * - 64
    - ENV_B_avg_count_at_A_shortest_dist
    - Average number of B atoms next to the A atoms at the shortest distance
  * - 65
    - ENV_B_avg_count_at_B_shortest_dist
    - Average number of B atoms next to the B atoms at the shortest distance
  * - 66
    - CN_AVG_coordination_number
    - Average coordination number
  * - 67
    - CN_AVG_A_atom_count
    - Average atom A number within CN
  * - 68
    - CN_AVG_B_atom_count
    - Average atom B number within CN
  * - 69
    - CN_AVG_polyhedron_volume
    - Average volume of polyhedra
  * - 70
    - CN_AVG_central_atom_to_center_of_mass_dist
    - Average distance from the central atom to the center of mass of polyhedron
  * - 71
    - CN_AVG_number_of_edges
    - Average number of edges of polyhedron
  * - 72
    - CN_AVG_number_of_faces
    - Average number of faces of polyhedron
  * - 73
    - CN_AVG_shortest_distance_to_face
    - Average shortest distance from central atom to center of face of polyhedron
  * - 74
    - CN_AVG_shortest_distance_to_edge
    - Average shortest distance from central atom to middle edge of polyhedron
  * - 75
    - CN_AVG_volume_of_inscribed_sphere
    - Average volume of inscribed sphere that could be fit in polyhedron
  * - 76
    - CN_AVG_packing_efficiency
    - Average packing efficiency of polyhedron
  * - 77
    - CN_MIN_coordination_number
    - Minimum coordination number
  * - 78
    - CN_MIN_A_atom_count
    - Minimum atom A number within CN
  * - 79
    - CN_MIN_B_atom_count
    - Minimum atom B number within CN
  * - 80
    - CN_MIN_polyhedron_volume
    - Minimum volume of polyhedra
  * - 81
    - CN_MIN_central_atom_to_center_of_mass_dist
    - Minimum distance from the central atom to the center of mass of polyhedron
  * - 82
    - CN_MIN_number_of_edges
    - Minimum number of edges of polyhedron
  * - 83
    - CN_MIN_number_of_faces
    - Minimum number of faces of polyhedron
  * - 84
    - CN_MIN_shortest_distance_to_face
    - Minimum shortest distance from central atom to center of face of polyhedron
  * - 85
    - CN_MIN_shortest_distance_to_edge
    - Minimum shortest distance from central atom to middle edge of polyhedron
  * - 86
    - CN_MIN_volume_of_inscribed_sphere
    - Minimum volume of inscribed sphere that could be fit in polyhedron
  * - 87
    - CN_MIN_packing_efficiency
    - Minimum packing efficiency of polyhedron
  * - 88
    - CN_MAX_coordination_number
    - Maximum coordination number
  * - 89
    - CN_MAX_A_atom_count
    - Maximum atom A number within CN
  * - 90
    - CN_MAX_B_atom_count
    - Maximum atom B number within CN
  * - 91
    - CN_MAX_polyhedron_volume
    - Maximum volume of polyhedra
  * - 92
    - CN_MAX_central_atom_to_center_of_mass_dist
    - Maximum distance from the central atom to the center of mass of polyhedron
  * - 93
    - CN_MAX_number_of_edges
    - Maximum number of edges of polyhedron
  * - 94
    - CN_MAX_number_of_faces
    - Maximum number of faces of polyhedron
  * - 95
    - CN_MAX_shortest_distance_to_face
    - Maximum shortest distance from central atom to center of face of polyhedron
  * - 96
    - CN_MAX_shortest_distance_to_edge
    - Maximum shortest distance from central atom to middle edge of polyhedron
  * - 97
    - CN_MAX_volume_of_inscribed_sphere
    - Maximum volume of inscribed sphere that could be fit in polyhedron
  * - 98
    - CN_MAX_packing_efficiency
    - Maximum packing efficiency of polyhedron

Ternary
-------

.. list-table::
    :header-rows: 1

    * - #
      - Feature
    * - 1
      - Entry
    * - 2
      - formula
    * - 3
      - R
    * - 4
      - M
    * - 5
      - X
    * - 6
      - INT_RR_dist
    * - 7
      - INT_MM_dist
    * - 8
      - INT_XX_dist
    * - 9
      - INT_RM_dist
    * - 10
      - INT_MX_dist
    * - 11
      - INT_RX_dist
    * - 12
      - INT_Rsize
    * - 13
      - INT_Msize
    * - 14
      - INT_Xsize
    * - 15
      - INT_Rsize_by_Msize
    * - 16
      - INT_Msize_by_Xsize
    * - 17
      - INT_Rsize_by_Xsize
    * - 18
      - INT_RR_dist_by_2_by_Rsize
    * - 19
      - INT_MM_dist_by_2_by_Msize
    * - 20
      - INT_XX_dist_by_2_by_Xsize
    * - 21
      - INT_RM_dist_by_RMsizes
    * - 22
      - INT_MX_dist_by_MXsizes
    * - 23
      - INT_RX_dist_by_RXsizes
    * - 24
      - INT_Rsize_ref
    * - 25
      - INT_Msize_ref
    * - 26
      - INT_Xsize_ref
    * - 27
      - INT_percent_diff_R_by_100
    * - 28
      - INT_percent_diff_M_by_100
    * - 29
      - INT_percent_diff_X_by_100
    * - 30
      - INT_RR_dist_minus_ref_diff
    * - 31
      - INT_MM_dist_minus_ref_diff
    * - 32
      - INT_XX_dist_minus_ref_diff
    * - 33
      - INT_RM_dist_minus_ref_diff
    * - 34
      - INT_MX_dist_minus_ref_diff
    * - 35
      - INT_RX_dist_minus_ref_diff
    * - 36
      - INT_R_factor
    * - 37
      - INT_UNI_shortest_homoatomic_dist
    * - 38
      - INT_UNI_shortest_heteroatomic_dist
    * - 39
      - INT_UNI_shortest_homoatomic_dist_by_2_by_atom_size
    * - 40
      - INT_UNI_shortest_heteroatomic_dist_by_sum_of_atom_sizes
    * - 41
      - INT_UNI_shortest_homoatomic_dist_by_2_by_refined_atom_size
    * - 42
      - INT_UNI_shortest_heteroatomic_dist_by_sum_of_refined_atom_sizes
    * - 43
      - INT_UNI_highest_refined_percent_diff_abs
    * - 44
      - INT_UNI_lowest_refined_percent_diff_abs
    * - 45
      - INT_UNI_packing_efficiency
    * - 46
      - WYC_R_lowest_wyckoff_label
    * - 47
      - WYC_M_lowest_wyckoff_label
    * - 48
      - WYC_X_lowest_wyckoff_label
    * - 49
      - WYC_identical_lowest_wyckoff_count
    * - 50
      - WYC_R_sites_total
    * - 51
      - WYC_M_sites_total
    * - 52
      - WYC_X_sites_total
    * - 53
      - WYC_R_multiplicity_total
    * - 54
      - WYC_M_multiplicity_total
    * - 55
      - WYC_X_multiplicity_total
    * - 56
      - ENV_R_shortest_dist_count
    * - 57
      - ENV_M_shortest_dist_count
    * - 58
      - ENV_X_shortest_dist_count
    * - 59
      - ENV_R_avg_shortest_dist_count
    * - 60
      - ENV_M_avg_shortest_dist_count
    * - 61
      - ENV_X_avg_shortest_dist_count
    * - 62
      - ENV_R_shortest_tol_dist_count
    * - 63
      - ENV_M_shortest_tol_dist_count
    * - 64
      - ENV_X_shortest_tol_dist_count
    * - 65
      - ENV_R_avg_shortest_dist_within_tol_count
    * - 66
      - ENV_M_avg_shortest_dist_within_tol_count
    * - 67
      - ENV_X_avg_shortest_dist_within_tol_count
    * - 68
      - ENV_R_second_by_first_shortest_dist
    * - 69
      - ENV_M_second_by_first_shortest_dist
    * - 70
      - ENV_X_second_by_first_shortest_dist
    * - 71
      - ENV_R_avg_second_by_first_shortest_dist
    * - 72
      - ENV_M_avg_second_by_first_shortest_dist
    * - 73
      - ENV_X_avg_second_by_first_shortest_dist
    * - 74
      - ENV_R_second_shortest_dist_count
    * - 75
      - ENV_M_second_shortest_dist_count
    * - 76
      - ENV_X_second_shortest_dist_count
    * - 77
      - ENV_R_avg_second_shortest_dist_count
    * - 78
      - ENV_M_avg_second_shortest_dist_count
    * - 79
      - ENV_X_avg_second_shortest_dist_count
    * - 80
      - ENV_R_homoatomic_dist_by_shortest_dist
    * - 81
      - ENV_M_homoatomic_dist_by_shortest_dist
    * - 82
      - ENV_X_homoatomic_dist_by_shortest_dist
    * - 83
      - ENV_R_avg_homoatomic_dist_by_shortest_dist
    * - 84
      - ENV_M_avg_homoatomic_dist_by_shortest_dist
    * - 85
      - ENV_X_avg_homoatomic_dist_by_shortest_dist
    * - 86
      - ENV_R_count_at_R_shortest_dist
    * - 87
      - ENV_R_count_at_M_shortest_dist
    * - 88
      - ENV_R_count_at_X_shortest_dist
    * - 89
      - ENV_R_avg_count_at_R_shortest_dist
    * - 90
      - ENV_R_avg_count_at_M_shortest_dist
    * - 91
      - ENV_R_avg_count_at_X_shortest_dist
    * - 92
      - ENV_M_count_at_R_shortest_dist
    * - 93
      - ENV_M_count_at_M_shortest_dist
    * - 94
      - ENV_M_count_at_X_shortest_dist
    * - 95
      - ENV_M_avg_count_at_R_shortest_dist
    * - 96
      - ENV_M_avg_count_at_M_shortest_dist
    * - 97
      - ENV_M_avg_count_at_X_shortest_dist
    * - 98
      - ENV_X_count_at_R_shortest_dist
    * - 99
      - ENV_X_count_at_M_shortest_dist
    * - 100
      - ENV_X_count_at_X_shortest_dist
    * - 101
      - ENV_X_avg_count_at_R_shortest_dist
    * - 102
      - ENV_X_avg_count_at_M_shortest_dist
    * - 103
      - ENV_X_avg_count_at_X_shortest_dist
    * - 104
      - CN_AVG_coordination_number
    * - 105
      - CN_AVG_R_atom_count
    * - 106
      - CN_AVG_M_atom_count
    * - 107
      - CN_AVG_X_atom_count
    * - 108
      - CN_AVG_polyhedron_volume
    * - 109
      - CN_AVG_central_atom_to_center_of_mass_dist
    * - 110
      - CN_AVG_number_of_edges
    * - 111
      - CN_AVG_number_of_faces
    * - 112
      - CN_AVG_shortest_distance_to_face
    * - 113
      - CN_AVG_shortest_distance_to_edge
    * - 114
      - CN_AVG_volume_of_inscribed_sphere
    * - 115
      - CN_AVG_packing_efficiency
    * - 116
      - CN_MIN_coordination_number
    * - 117
      - CN_MIN_R_atom_count
    * - 118
      - CN_MIN_M_atom_count
    * - 119
      - CN_MIN_X_atom_count
    * - 120
      - CN_MIN_polyhedron_volume
    * - 121
      - CN_MIN_central_atom_to_center_of_mass_dist
    * - 122
      - CN_MIN_number_of_edges
    * - 123
      - CN_MIN_number_of_faces
    * - 124
      - CN_MIN_shortest_distance_to_face
    * - 125
      - CN_MIN_shortest_distance_to_edge
    * - 126
      - CN_MIN_volume_of_inscribed_sphere
    * - 127
      - CN_MIN_packing_efficiency
    * - 128
      - CN_MAX_coordination_number
    * - 129
      - CN_MAX_R_atom_count
    * - 130
      - CN_MAX_M_atom_count
    * - 131
      - CN_MAX_X_atom_count
    * - 132
      - CN_MAX_polyhedron_volume
    * - 133
      - CN_MAX_central_atom_to_center_of_mass_dist
    * - 134
      - CN_MAX_number_of_edges
    * - 135
      - CN_MAX_number_of_faces
    * - 136
      - CN_MAX_shortest_distance_to_face
    * - 137
      - CN_MAX_shortest_distance_to_edge
    * - 138
      - CN_MAX_volume_of_inscribed_sphere
    * - 139
      - CN_MAX_packing_efficiency


Quaternary
----------

.. list-table::
  :header-rows: 1

  * - #
    - Feature
  * - 1
    - Entry
  * - 2
    - Formula
  * - 3
    - Structure
  * - 4
    - A
  * - 5
    - B
  * - 6
    - C
  * - 7
    - D
  * - 8
    - INT_AA_dist
  * - 9
    - INT_BB_dist
  * - 10
    - INT_CC_dist
  * - 11
    - INT_DD_dist
  * - 12
    - INT_AB_dist
  * - 13
    - INT_AC_dist
  * - 14
    - INT_AD_dist
  * - 15
    - INT_BC_dist
  * - 16
    - INT_BD_dist
  * - 17
    - INT_CD_dist
  * - 18
    - INT_Asize
  * - 19
    - INT_Bsize
  * - 20
    - INT_Csize
  * - 21
    - INT_Dsize
  * - 22
    - INT_Asize_by_Bsize
  * - 23
    - INT_Bsize_by_Csize
  * - 24
    - INT_Csize_by_Dsize
  * - 25
    - INT_Asize_by_Csize
  * - 26
    - INT_Asize_by_Dsize
  * - 27
    - INT_Bsize_by_Dsize
  * - 28
    - INT_AA_dist_by_2_by_Asize
  * - 29
    - INT_BB_dist_by_2_by_Bsize
  * - 30
    - INT_CC_dist_by_2_by_Csize
  * - 31
    - INT_DD_dist_by_2_by_Dsize
  * - 32
    - INT_AB_dist_by_ABsizes
  * - 33
    - INT_AC_dist_by_ACsizes
  * - 34
    - INT_AD_dist_by_ADsizes
  * - 35
    - INT_BC_dist_by_BCsizes
  * - 36
    - INT_BD_dist_by_BDsizes
  * - 37
    - INT_CD_dist_by_CDsizes
  * - 38
    - INT_Asize_ref
  * - 39
    - INT_Bsize_ref
  * - 40
    - INT_Csize_ref
  * - 41
    - INT_Dsize_ref
  * - 42
    - INT_percent_diff_A_by_100
  * - 43
    - INT_percent_diff_B_by_100
  * - 44
    - INT_percent_diff_C_by_100
  * - 45
    - INT_percent_diff_D_by_100
  * - 46
    - INT_AA_minus_ref_diff
  * - 47
    - INT_BB_minus_ref_diff
  * - 48
    - INT_CC_minus_ref_diff
  * - 49
    - INT_DD_minus_ref_diff
  * - 50
    - INT_AB_minus_ref_diff
  * - 51
    - INT_AC_minus_ref_diff
  * - 52
    - INT_AD_minus_ref_diff
  * - 53
    - INT_BC_minus_ref_diff
  * - 54
    - INT_BD_minus_ref_diff
  * - 55
    - INT_CD_minus_ref_diff
  * - 56
    - INT_R_factor
  * - 57
    - INT_UNI_shortest_homoatomic_dist
  * - 58
    - INT_UNI_shortest_heteroatomic_dist
  * - 59
    - INT_UNI_shortest_homoatomic_dist_by_2_by_atom_size
  * - 60
    - INT_UNI_shortest_heteroatomic_dist_by_sum_of_atom_sizes
  * - 61
    - INT_UNI_shortest_homoatomic_dist_by_2_by_refined_atom_size
  * - 62
    - INT_UNI_shortest_heteroatomic_dist_by_sum_of_refined_atom_sizes
  * - 63
    - INT_UNI_highest_refined_percent_diff_abs
  * - 64
    - INT_UNI_lowest_refined_percent_diff_abs
  * - 65
    - INT_UNI_refined_packing_efficiency
  * - 66
    - WYK_A_lowest_wyckoff
  * - 67
    - WYK_B_lowest_wyckoff
  * - 68
    - WYK_C_lowest_wyckoff
  * - 69
    - WYK_D_lowest_wyckoff
  * - 70
    - WYK_identical_lowest_wyckoff_count
  * - 71
    - WYK_A_sites_total
  * - 72
    - WYK_B_sites_total
  * - 73
    - WYK_C_sites_total
  * - 74
    - WYK_D_sites_total
  * - 75
    - WYK_A_multiplicity_total
  * - 76
    - WYK_B_multiplicity_total
  * - 77
    - WYK_C_multiplicity_total
  * - 78
    - WYK_D_multiplicity_total
  * - 79
    - ENV_A_shortest_dist_count
  * - 80
    - ENV_B_shortest_dist_count
  * - 81
    - ENV_C_shortest_dist_count
  * - 82
    - ENV_D_shortest_dist_count
  * - 83
    - ENV_A_avg_shortest_dist_count
  * - 84
    - ENV_B_avg_shortest_dist_count
  * - 85
    - ENV_C_avg_shortest_dist_count
  * - 86
    - ENV_D_avg_shortest_dist_count
  * - 87
    - ENV_A_shortest_tol_dist_count
  * - 88
    - ENV_B_shortest_tol_dist_count
  * - 89
    - ENV_C_shortest_tol_dist_count
  * - 90
    - ENV_D_shortest_tol_dist_count
  * - 91
    - ENV_A_avg_shortest_dist_within_tol_count
  * - 92
    - ENV_B_avg_shortest_dist_within_tol_count
  * - 93
    - ENV_C_avg_shortest_dist_within_tol_count
  * - 94
    - ENV_D_avg_shortest_dist_within_tol_count
  * - 95
    - ENV_A_second_by_first_shortest_dist
  * - 96
    - ENV_B_second_by_first_shortest_dist
  * - 97
    - ENV_C_second_by_first_shortest_dist
  * - 98
    - ENV_D_second_by_first_shortest_dist
  * - 99
    - ENV_A_avg_second_by_first_shortest_dist
  * - 100
    - ENV_B_avg_second_by_first_shortest_dist
  * - 101
    - ENV_C_avg_second_by_first_shortest_dist
  * - 102
    - ENV_D_avg_second_by_first_shortest_dist
  * - 103
    - ENV_A_second_shortest_dist_count
  * - 104
    - ENV_B_second_shortest_dist_count
  * - 105
    - ENV_C_second_shortest_dist_count
  * - 106
    - ENV_D_second_shortest_dist_count
  * - 107
    - ENV_A_avg_second_shortest_dist_count
  * - 108
    - ENV_B_avg_second_shortest_dist_count
  * - 109
    - ENV_C_avg_second_shortest_dist_count
  * - 110
    - ENV_D_avg_second_shortest_dist_count
  * - 111
    - ENV_A_homoatomic_dist_by_shortest_dist
  * - 112
    - ENV_B_homoatomic_dist_by_shortest_dist
  * - 113
    - ENV_C_homoatomic_dist_by_shortest_dist
  * - 114
    - ENV_D_homoatomic_dist_by_shortest_dist
  * - 115
    - ENV_A_avg_homoatomic_dist_by_shortest_dist
  * - 116
    - ENV_B_avg_homoatomic_dist_by_shortest_dist
  * - 117
    - ENV_C_avg_homoatomic_dist_by_shortest_dist
  * - 118
    - ENV_D_avg_homoatomic_dist_by_shortest_dist
  * - 119
    - ENV_A_count_at_A_shortest_dist
  * - 120
    - ENV_B_count_at_A_shortest_dist
  * - 121
    - ENV_C_count_at_A_shortest_dist
  * - 122
    - ENV_D_count_at_A_shortest_dist
  * - 123
    - ENV_A_avg_count_at_A_shortest_dist
  * - 124
    - ENV_B_avg_count_at_A_shortest_dist
  * - 125
    - ENV_C_avg_count_at_A_shortest_dist
  * - 126
    - ENV_D_avg_count_at_A_shortest_dist
  * - 127
    - ENV_A_count_at_B_shortest_dist
  * - 128
    - ENV_B_count_at_B_shortest_dist
  * - 129
    - ENV_C_count_at_B_shortest_dist
  * - 130
    - ENV_D_count_at_B_shortest_dist
  * - 131
    - ENV_A_avg_count_at_B_shortest_dist
  * - 132
    - ENV_B_avg_count_at_B_shortest_dist
  * - 133
    - ENV_C_avg_count_at_B_shortest_dist
  * - 134
    - ENV_D_avg_count_at_B_shortest_dist
  * - 135
    - ENV_A_count_at_C_shortest_dist
  * - 136
    - ENV_B_count_at_C_shortest_dist
  * - 137
    - ENV_C_count_at_C_shortest_dist
  * - 138
    - ENV_D_count_at_C_shortest_dist
  * - 139
    - ENV_A_avg_count_at_C_shortest_dist
  * - 140
    - ENV_B_avg_count_at_C_shortest_dist
  * - 141
    - ENV_C_avg_count_at_C_shortest_dist
  * - 142
    - ENV_D_avg_count_at_C_shortest_dist
  * - 143
    - ENV_A_count_at_D_shortest_dist
  * - 144
    - ENV_B_count_at_D_shortest_dist
  * - 145
    - ENV_C_count_at_D_shortest_dist
  * - 146
    - ENV_D_count_at_D_shortest_dist
  * - 147
    - ENV_A_avg_count_at_D_shortest_dist
  * - 148
    - ENV_B_avg_count_at_D_shortest_dist
  * - 149
    - ENV_C_avg_count_at_D_shortest_dist
  * - 150
    - ENV_D_avg_count_at_D_shortest_dist
  * - 151
    - CN_AVG_coordination_number
  * - 152
    - CN_AVG_A_atom_count
  * - 153
    - CN_AVG_B_atom_count
  * - 154
    - CN_AVG_C_atom_count
  * - 155
    - CN_AVG_D_atom_count
  * - 156
    - CN_AVG_polyhedron_volume
  * - 157
    - CN_AVG_central_atom_to_center_of_mass_dist
  * - 158
    - CN_AVG_number_of_edges
  * - 159
    - CN_AVG_number_of_faces
  * - 160
    - CN_AVG_shortest_distance_to_face
  * - 161
    - CN_AVG_shortest_distance_to_edge
  * - 162
    - CN_AVG_volume_of_inscribed_sphere
  * - 163
    - CN_AVG_packing_efficiency
  * - 164
    - CN_MIN_coordination_number
  * - 165
    - CN_MIN_A_atom_count
  * - 166
    - CN_MIN_B_atom_count
  * - 167
    - CN_MIN_C_atom_count
  * - 168
    - CN_MIN_D_atom_count
  * - 169
    - CN_MIN_polyhedron_volume
  * - 170
    - CN_MIN_central_atom_to_center_of_mass_dist
  * - 171
    - CN_MIN_number_of_edges
  * - 172
    - CN_MIN_number_of_faces
  * - 173
    - CN_MIN_shortest_distance_to_face
  * - 174
    - CN_MIN_shortest_distance_to_edge
  * - 175
    - CN_MIN_volume_of_inscribed_sphere
  * - 176
    - CN_MIN_packing_efficiency
  * - 177
    - CN_MAX_coordination_number
  * - 178
    - CN_MAX_A_atom_count
  * - 179
    - CN_MAX_B_atom_count
  * - 180
    - CN_MAX_C_atom_count
  * - 181
    - CN_MAX_D_atom_count
  * - 182
    - CN_MAX_polyhedron_volume
  * - 183
    - CN_MAX_central_atom_to_center_of_mass_dist
  * - 184
    - CN_MAX_number_of_edges
  * - 185
    - CN_MAX_number_of_faces
  * - 186
    - CN_MAX_shortest_distance_to_face
  * - 187
    - CN_MAX_shortest_distance_to_edge
  * - 188
    - CN_MAX_volume_of_inscribed_sphere
  * - 189
    - CN_MAX_packing_efficiency
