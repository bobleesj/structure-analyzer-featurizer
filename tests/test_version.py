"""Unit tests for __version__.py."""

import structure_analyzer_featurizer  # noqa


def test_package_version():
    """Ensure the package version is defined and not set to the initial
    placeholder."""
    assert hasattr(structure_analyzer_featurizer, "__version__")
    assert structure_analyzer_featurizer.__version__ != "0.0.0"
