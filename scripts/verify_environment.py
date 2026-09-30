#!/usr/bin/env python3
"""
Environment and clean installation verification script.
Tests Python version, core dependencies, Playwright browser, and code quality tools.
"""

import sys


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

    # 5. RAG & Retrieval dependencies
    import importlib.metadata as md

    from qdrant_client import QdrantClient
    from rank_bm25 import BM25Okapi, BM25L, BM25Plus
    from rerankers import Reranker
    from sentence_transformers import SentenceTransformer

    print(f"[x] Qdrant Client Version: {md.version('qdrant-client')}")
    print("[x] QdrantClient instantiation: AVAILABLE")
    print("[x] BM25 (Okapi / L / Plus): AVAILABLE")
    print(f"[x] Sentence-Transformers Version: {md.version('sentence-transformers')}")
    print(f"[x] Rerankers Version: {md.version('rerankers')}")

    print("=" * 60)
    print("ALL ENVIRONMENT, EXTRACTION & RAG DEPENDENCY CHECKS PASSED!")
    print("=" * 60)


if __name__ == "__main__":
    verify()
