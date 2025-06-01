"""Unit tests for __version__.py."""

import SAF


def test_package_version():
    """Ensure the package version is defined and not set to the initial
    placeholder."""
    assert hasattr(SAF, "__version__")
    assert SAF.__version__ != "0.0.0"
