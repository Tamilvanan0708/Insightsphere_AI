"""
InsightSphere AI - Configuration Module
Loads application configuration and Gemini / embedding settings from environment variables.
"""

from functools import lru_cache

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Application configuration loaded from environment variables."""

    # -------------------------------------------------------------------------
    # 1. Gemini LLM Configuration
    # -------------------------------------------------------------------------
    gemini_api_key: str = Field(
        default="",
        validation_alias="GEMINI_API_KEY",
        description="Google Gemini API key for model reasoning and generation",
    )
    gemini_model: str = Field(
        default="gemini-1.5-flash",
        validation_alias="GEMINI_MODEL",
        description="Primary Gemini model for agent reasoning, analysis, and validation",
    )
    gemini_pro_model: str = Field(
        default="gemini-1.5-pro",
        validation_alias="GEMINI_PRO_MODEL",
        description="Gemini Pro model for complex synthesis and report generation",
    )
    gemini_temperature: float = Field(
        default=0.7,
        validation_alias="GEMINI_TEMPERATURE",
        description="Sampling temperature for Gemini models",
    )
    gemini_max_output_tokens: int | None = Field(
        default=2048,
        validation_alias="GEMINI_MAX_OUTPUT_TOKENS",
        description="Max generation tokens",
    )

    # -------------------------------------------------------------------------
    # 2. Embedding Configuration (RAG Pipeline)
    # -------------------------------------------------------------------------
    gemini_embedding_model: str = Field(
        default="text-embedding-004",
        validation_alias="GEMINI_EMBEDDING_MODEL",
        description="Gemini embedding model for RAG chunk indexing and retrieval",
    )
    embedding_dimension: int = Field(
        default=768,
        validation_alias="EMBEDDING_DIMENSION",
        description="Dimensionality of the embedding vectors (768 for text-embedding-004)",
    )

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )


@lru_cache
def get_settings() -> Settings:
    """Return a cached singleton instance of Settings."""
    return Settings()
