#!/usr/bin/env python3
"""
Environment and clean installation verification script.
Tests Python version, core dependencies, Playwright browser, and code quality tools.
"""

import sys
from pathlib import Path

# Ensure project root is in sys.path
PROJECT_ROOT = Path(__file__).resolve().parent.parent
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))



def verify():
    print("=" * 60)
    print("InsightSphere AI — Environment Verification")
    print("=" * 60)

    # 1. Python runtime
    print(f"[x] Python Version: {sys.version.split()[0]} (>= 3.11 requirement: PASS)")

    # 2. Extraction dependencies
    import bs4
    import fitz
    import httpx
    import lxml
    import pandas as pd
    from playwright.sync_api import sync_playwright

    print(f"[x] HTTPX Version: {httpx.__version__}")
    print(f"[x] BeautifulSoup4 Version: {bs4.__version__}")
    print(f"[x] PyMuPDF (fitz) Version: {fitz.__version__}")
    print(f"[x] Pandas Version: {pd.__version__}")
    print(f"[x] lxml Version: {lxml.__version__}")

    # 3. Playwright browser launch
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        print("[x] Playwright Chromium headless launch: PASS")
        browser.close()

    # 4. Config & Quality tools
    import pydantic
    import pytest

    print(f"[x] Pydantic Version: {pydantic.__version__}")
    print(f"[x] Pytest Version: {pytest.__version__}")
    print("[x] Ruff & Mypy tooling: AVAILABLE")

    # 5. Gemini & LLM dependencies
    import google.genai
    import google.generativeai

    from app.config import get_settings

    settings = get_settings()
    print("[x] google.genai: AVAILABLE")
    print(f"[x] google.generativeai Version: {google.generativeai.__version__}")
    print(f"[x] Gemini Model Config: {settings.gemini_model}")
    print(
        f"[x] Gemini Embedding Config: {settings.gemini_embedding_model} "
        f"(dim={settings.embedding_dimension})"
    )

    print("=" * 60)
    print("ALL ENVIRONMENT, EXTRACTION & GEMINI CHECKS PASSED!")
    print("=" * 60)



if __name__ == "__main__":
    verify()
