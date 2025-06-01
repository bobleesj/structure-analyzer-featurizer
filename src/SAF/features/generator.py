# Given a binary cif, generate all the features
from SAF.features import (
    binary_env_handler,
    binary_interatomic,
    binary_wyc,
    coordination_handler,
    ternary_env_handler,
    ternary_interatomic,
    ternary_wyc,
)


def generate_binary_features(cif):
    binary_int_data, uni_int_data = (
        binary_interatomic.compute_binary_interatomic_features(cif)
    )
    binary_wyc_data, uni_wyc_data = binary_wyc.compute_binary_wyc_features(cif)
    binary_env_data = binary_env_handler.compute_binary_env_features(cif)
    binary_CN_data = coordination_handler.get_CN_binary_features(cif)

    # Combine all features into a single dictionary
    binary_combined_data = {}
    binary_combined_data.update(binary_int_data)
    binary_combined_data.update(binary_wyc_data)
    binary_combined_data.update(binary_env_data)
    binary_combined_data.update(binary_CN_data)

    # Get universal features
    uni_combined_data = {}
    uni_combined_data.update(uni_int_data)
    uni_combined_data.update(uni_wyc_data)
    uni_combined_data.update(binary_CN_data)
    print(binary_combined_data)
    print(uni_combined_data)

    return binary_combined_data, uni_combined_data


def generate_ternary_features(cif):
    ternary_int_data, uni_int_data = (
        ternary_interatomic.compute_ternary_interatomic_features(cif)
    )
    ternary_wyc_data, uni_wyc_data = ternary_wyc.compute_ternary_wyk_features(
        cif
    )
    ternary_env_data = ternary_env_handler.compute_ternary_env_features(cif)
    ternary_CN_data = coordination_handler.get_CN_ternary_features(cif)

    ternary_combined_data = {}
    ternary_combined_data.update(ternary_int_data)
    ternary_combined_data.update(ternary_wyc_data)
    ternary_combined_data.update(ternary_env_data)
    ternary_combined_data.update(ternary_CN_data)

    # Get universal features
    uni_combined_data = {}
    uni_combined_data.update(uni_int_data)
    uni_combined_data.update(uni_wyc_data)
    uni_combined_data.update(ternary_CN_data)
