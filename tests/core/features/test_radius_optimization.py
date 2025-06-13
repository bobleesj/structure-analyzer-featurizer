from core.data.radius_handler import get_CIF_pauling_radius

def test_binary_optimization(ThSb_cif):
    data = get_CIF_pauling_radius(["Th", "Sb"])
    assert data ==  {
        'Sb': {'CIF_radius': 1.434, 'Pauling_radius_CN12': 1.59},
          'Th': {'CIF_radius': 1.798, 'Pauling_radius_CN12': 1.795}}
    
    
    