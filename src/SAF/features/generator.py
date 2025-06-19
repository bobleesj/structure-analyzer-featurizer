from bobleesj.utils.sorters.elements import Elements
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


def _generate_features(
    file_path: str, supercell_size: int, use_size_constraint: bool, custom_labels, int_module, wyc_module, env_module, CN_module
):
    cif = Cif(file_path, supercell_size=supercell_size, compute_CN=True)
    elements = list(cif.unique_elements)
    element_sorter = Elements(label_mapping=custom_labels)
    if custom_labels:
        elements_sorted = element_sorter.sort(elements, method="custom")
    else:
        elements_sorted = element_sorter.sort(elements, method="mendeleev")
    elements_tuple = tuple(elements_sorted)
    int_feat, int_uni = int_module.compute_features(cif, use_size_constraint, elements_tuple)
    wyc_feat, wyc_uni = wyc_module.compute_features(cif, elements_sorted)
    env_feat = env_module.compute_features(cif, elements_sorted)
    CN_feat = CN_module.compute_features(cif, elements_sorted)
    features = {
        **int_feat,
        **wyc_feat,
        **env_feat,
        **CN_feat,
    }
    uni_features = {
        **int_uni,
        **wyc_uni,
    }
    return features, uni_features


def compute_binary_features(file_path: str, supercell_size=3, use_size_constraint=True, custom_labels=None):
    return _generate_features(
        file_path,
        supercell_size,
        use_size_constraint,
        custom_labels=custom_labels,
        int_module=int_binary,
        wyc_module=wyc_binary,
        env_module=env_binary,
        CN_module=CN_binary,
    )


def compute_ternary_features(file_path: str, supercell_size=3, use_size_constraint=True, custom_labels=None):
    return _generate_features(
        file_path,
        supercell_size,
        use_size_constraint,
        custom_labels=custom_labels,
        int_module=int_ternary,
        wyc_module=wyc_ternary,
        env_module=env_ternary,
        CN_module=CN_ternary,
    )


def compute_quaternary_features(file_path: str, supercell_size=3, use_size_constraint=True, custom_labels=None):
    return _generate_features(
        file_path,
        supercell_size,
        use_size_constraint,
        custom_labels=custom_labels,
        int_module=int_quaternary,
        wyc_module=wyc_quaternary,
        env_module=env_quaternary,
        CN_module=CN_quaternary,
    )
