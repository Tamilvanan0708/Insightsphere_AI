"""
Gemini Client & Connectivity Utility for InsightSphere AI.
Handles initializing Google GenAI client and verifying connectivity.
"""

from typing import Any

from google import genai

from app.config import Settings, get_settings


def get_genai_client(
    api_key: str | None = None, settings: Settings | None = None
) -> genai.Client:
    """Initialize and return a google.genai.Client instance.

    Uses provided api_key or falls back to settings.
    Credentials are never hardcoded.
    """
    cfg = settings or get_settings()
    key = api_key or cfg.gemini_api_key

    if not key:
        raise ValueError(
            "GEMINI_API_KEY is not set. Please provide it via environment variable "
            "or .env file."
        )

    return genai.Client(api_key=key)


def get_embedding_config(settings: Settings | None = None) -> dict[str, Any]:
    """Retrieve Gemini embedding configuration for the RAG pipeline."""
    cfg = settings or get_settings()
    return {
        "model": cfg.gemini_embedding_model,
        "dimension": cfg.embedding_dimension,
    }


def test_gemini_connection(
    api_key: str | None = None,
    settings: Settings | None = None,
) -> dict[str, Any]:
    """Test connectivity to Google Gemini API.

    Returns a status dictionary with details.
    """
    cfg = settings or get_settings()
    key = api_key or cfg.gemini_api_key

    if not key:
        return {
            "status": "error",
            "connected": False,
            "message": "GEMINI_API_KEY is empty. Set GEMINI_API_KEY in .env.",
        }

    try:
        client = get_genai_client(api_key=key, settings=cfg)
        # Verify connection by generating a lightweight test response
        response = client.models.generate_content(
            model=cfg.gemini_model,
            contents="Ping",
        )
        return {
            "status": "ok",
            "connected": True,
            "model": cfg.gemini_model,
            "response_preview": (response.text or "").strip()[:50],
        }
    except Exception as exc:
        return {
            "status": "error",
            "connected": False,
            "message": str(exc),
        }
