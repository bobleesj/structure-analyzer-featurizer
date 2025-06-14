from cifkit import Cif
from SAF.features.interatomic import binary as int_binary
from SAF.features.wyc import binary as wyc_binary
from SAF.features.environment import binary as env_binary
from SAF.features.coordination import binary as CN_binary


def generate_features(file_path: str):
    cif = Cif(file_path)
    cif.compute_connections()
    cif.compute_CN()
    int, int_uni = int_binary.compute_features(cif)
    wyc, wyc_uni = wyc_binary.compute_features(cif)
    env = env_binary.compute_features(cif)
    CN = CN_binary.compute_features(cif)
    
    features = {
        **int,
        **wyc,
        **env,
        **CN,
    }
    
    uni_features = {
        **int_uni,
        **wyc_uni,
    }
    return features, uni_features