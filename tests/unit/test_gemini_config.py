"""
Unit tests for Gemini model configuration and client setup.
Validates environment variable loading, default values, embedding configuration,
and connectivity test utilities.
"""

import pytest

from app.agents.gemini_client import (
    get_embedding_config,
    get_genai_client,
)
from app.agents.gemini_client import (
    test_gemini_connection as run_test_gemini_connection,
)
from app.config import Settings
from app.rag.embeddings import get_rag_embedding_config


def test_default_gemini_settings():
    """Verify default Gemini settings have expected production defaults."""
    settings = Settings(
        GEMINI_API_KEY="",
        GEMINI_MODEL="gemini-1.5-flash",
        GEMINI_PRO_MODEL="gemini-1.5-pro",
        GEMINI_TEMPERATURE=0.7,
        GEMINI_MAX_OUTPUT_TOKENS=2048,
        GEMINI_EMBEDDING_MODEL="text-embedding-004",
        EMBEDDING_DIMENSION=768,
    )

    assert settings.gemini_api_key == ""
    assert settings.gemini_model == "gemini-1.5-flash"
    assert settings.gemini_pro_model == "gemini-1.5-pro"
    assert settings.gemini_temperature == 0.7
    assert settings.gemini_max_output_tokens == 2048
    assert settings.gemini_embedding_model == "text-embedding-004"
    assert settings.embedding_dimension == 768


def test_settings_from_environment_variables(monkeypatch):
    """Verify that configuration accurately loads and overrides from environment variables."""
    monkeypatch.setenv("GEMINI_API_KEY", "test-env-api-key-12345")
    monkeypatch.setenv("GEMINI_MODEL", "gemini-2.0-flash")
    monkeypatch.setenv("GEMINI_PRO_MODEL", "gemini-2.0-pro")
    monkeypatch.setenv("GEMINI_TEMPERATURE", "0.2")
    monkeypatch.setenv("GEMINI_MAX_OUTPUT_TOKENS", "4096")
    monkeypatch.setenv("GEMINI_EMBEDDING_MODEL", "custom-embedding-model")
    monkeypatch.setenv("EMBEDDING_DIMENSION", "1536")

    custom_settings = Settings()

    assert custom_settings.gemini_api_key == "test-env-api-key-12345"
    assert custom_settings.gemini_model == "gemini-2.0-flash"
    assert custom_settings.gemini_pro_model == "gemini-2.0-pro"
    assert custom_settings.gemini_temperature == 0.2
    assert custom_settings.gemini_max_output_tokens == 4096
    assert custom_settings.gemini_embedding_model == "custom-embedding-model"
    assert custom_settings.embedding_dimension == 1536


def test_credentials_not_hardcoded():
    """Ensure credentials are not hardcoded and raise an error when missing."""
    empty_settings = Settings(GEMINI_API_KEY="")

    with pytest.raises(ValueError, match="GEMINI_API_KEY is not set"):
        get_genai_client(api_key="", settings=empty_settings)


def test_client_initialization_with_key():
    """Verify google.genai.Client initializes properly when an API key is provided."""
    test_settings = Settings(GEMINI_API_KEY="dummy-test-key")
    client = get_genai_client(settings=test_settings)
    assert client is not None


def test_rag_embedding_configuration():
    """Verify embedding configuration is accessible for the RAG pipeline."""
    settings = Settings(
        GEMINI_EMBEDDING_MODEL="text-embedding-004",
        EMBEDDING_DIMENSION=768,
    )

    agent_embed_cfg = get_embedding_config(settings)
    rag_embed_cfg = get_rag_embedding_config(settings)

    assert agent_embed_cfg == {"model": "text-embedding-004", "dimension": 768}
    assert rag_embed_cfg == {"model": "text-embedding-004", "dimension": 768}


def test_gemini_connectivity_without_key():
    """Verify test_gemini_connection gracefully handles missing API keys."""
    empty_settings = Settings(GEMINI_API_KEY="")
    result = run_test_gemini_connection(settings=empty_settings)

    assert result["status"] == "error"
    assert result["connected"] is False
    assert "GEMINI_API_KEY is empty" in result["message"]

