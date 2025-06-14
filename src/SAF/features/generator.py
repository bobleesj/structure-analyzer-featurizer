from cifkit import Cif

from SAF.features.coordination import binary as CN_binary
from SAF.features.coordination import quaternary as CN_quaternary
from SAF.features.coordination import ternary as CN_ternary
from SAF.features.environment import binary as env_binary
from SAF.features.environment import quaternary as env_quaternary
from SAF.features.environment import ternary as env_ternary
from SAF.features.interatomic import binary as int_binary
from SAF.features.interatomic import quaternary as int_quaternary
from SAF.features.interatomic import ternary as int_ternary
from SAF.features.wyc import binary as wyc_binary
from SAF.features.wyc import quaternary as wyc_quaternary
from SAF.features.wyc import ternary as wyc_ternary

# FIXME: refactor this


def generate_binary_features(file_path: str):
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


def generate_ternary_features(file_path: str):
    cif = Cif(file_path)
    cif.compute_connections()
    cif.compute_CN()
    int, int_uni = int_ternary.compute_features(cif)
    wyc, wyc_uni = wyc_ternary.compute_features(cif)
    env = env_ternary.compute_features(cif)
    CN = CN_ternary.compute_features(cif)

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


def generate_quaternary_features(file_path: str):
    cif = Cif(file_path)
    cif.compute_connections()
    cif.compute_CN()
    int, int_uni = int_quaternary.compute_features(cif)
    wyc, wyc_uni = wyc_quaternary.compute_features(cif)
    env = env_quaternary.compute_features(cif)
    CN = CN_quaternary.compute_features(cif)

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
