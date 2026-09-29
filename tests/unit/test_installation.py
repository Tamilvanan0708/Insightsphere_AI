"""Test verification of Python runtime and installed dependencies."""

import sys


def test_python_version():
    """Verify Python runtime is 3.11 or higher."""
    assert sys.version_info >= (3, 11), f"Expected Python >= 3.11, got {sys.version}"


def test_extraction_imports():
    """Verify core extraction libraries import successfully."""
    import bs4
    import fitz  # PyMuPDF
    import httpx
    import lxml
    import pandas as pd
    from playwright.sync_api import sync_playwright

    assert httpx.__version__
    assert bs4.__version__
    assert fitz.__version__
    assert pd.__version__
    assert lxml.__version__

    # Test Playwright launch
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        assert browser is not None
        browser.close()


def test_configuration_imports():
    """Verify configuration and environment tools import."""
    import dotenv
    import pydantic
    import pydantic_settings

    assert dotenv.__name__ == "dotenv"
    assert pydantic.__version__
    assert pydantic_settings.__name__ == "pydantic_settings"
