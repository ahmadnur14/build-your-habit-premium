"""
Project configuration for Build Your Habit Premium
"""
from pathlib import Path


class Config:
    """Simple configuration container with project paths and defaults."""

    APP_NAME = "Build Your Habit Premium"
    VERSION = "0.1.0"
    BASE_DIR = Path(__file__).parent.resolve()
    DATA_DIR = BASE_DIR / "data"
    SRC_DIR = BASE_DIR / "src"
    TESTS_DIR = BASE_DIR / "tests"
    REQUIREMENTS_FILE = BASE_DIR / "requirements.txt"
    LOG_LEVEL = "INFO"


def ensure_dirs():
    """Create common project directories if they don't exist."""
    for d in (Config.DATA_DIR, Config.SRC_DIR, Config.TESTS_DIR):
        d.mkdir(parents=True, exist_ok=True)


if __name__ == "__main__":
    ensure_dirs()
