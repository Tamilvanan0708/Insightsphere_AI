#!/usr/bin/env python3
"""
Test Gemini model connectivity and configuration.
Usage:
    python scripts/test_gemini_connection.py
"""

import sys
from pathlib import Path

# Ensure project root is in sys.path
PROJECT_ROOT = Path(__file__).resolve().parent.parent
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from app.agents.gemini_client import get_embedding_config, test_gemini_connection  # noqa: E402
from app.config import get_settings  # noqa: E402


def main():
    print("=" * 60)
    print("InsightSphere AI — Gemini Connectivity & Configuration Test")
    print("=" * 60)

    settings = get_settings()
    print(f"Configured Gemini Model:     {settings.gemini_model}")
    print(f"Configured Gemini Pro Model: {settings.gemini_pro_model}")
    print(f"Configured Temperature:      {settings.gemini_temperature}")
    print(f"Configured Max Tokens:       {settings.gemini_max_output_tokens}")
    print(f"Configured Embedding Model:  {settings.gemini_embedding_model}")
    print(f"Configured Embedding Dim:    {settings.embedding_dimension}")

    has_key = bool(
        settings.gemini_api_key and settings.gemini_api_key != "your_gemini_api_key_here"
    )
    masked_key = (
        f"{settings.gemini_api_key[:4]}...{settings.gemini_api_key[-4:]}"
        if has_key and len(settings.gemini_api_key) > 8
        else ("NOT SET" if not settings.gemini_api_key else "TEMPLATE VALUE")
    )
    print(f"API Key Status:              {masked_key}")

    embedding_cfg = get_embedding_config(settings)
    print(f"RAG Embedding Configuration: {embedding_cfg}")

    print("-" * 60)
    if not has_key:
        print("[!] No live GEMINI_API_KEY detected in environment or .env file.")
        print("[!] Skipping live API network call. Configuration check passed successfully.")
        print("=" * 60)
        return 0

    print("Testing live Gemini API connectivity...")
    result = test_gemini_connection(settings=settings)
    if result["connected"]:
        print(f"[x] Successfully connected to Gemini! Preview: {result.get('response_preview')}")
        print("=" * 60)
        return 0
    else:
        print(f"[!] Connectivity test failed: {result.get('message')}")
        print("=" * 60)
        return 1


if __name__ == "__main__":
    sys.exit(main())
