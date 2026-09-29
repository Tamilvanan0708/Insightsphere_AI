"""
RAG Embedding Configuration & Helpers for InsightSphere AI.
Provides settings and utilities for generating embeddings via Gemini text-embedding models.
"""

from typing import Any

from app.config import Settings, get_settings


def get_rag_embedding_config(settings: Settings | None = None) -> dict[str, Any]:
    """Retrieve Gemini embedding configuration for the RAG pipeline."""
    cfg = settings or get_settings()
    return {
        "model": cfg.gemini_embedding_model,
        "dimension": cfg.embedding_dimension,
    }
