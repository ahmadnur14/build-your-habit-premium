"""
Utility helpers for Build Your Habit Premium
"""
import json
import logging
from pathlib import Path
from typing import Any, Dict

from config import Config


def setup_logging(level: str = None):
    level = level or Config.LOG_LEVEL
    numeric_level = getattr(logging, level.upper(), logging.INFO)
    logging.basicConfig(
        level=numeric_level,
        format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
    )


def read_json(path: Path) -> Dict[str, Any]:
    if not path.exists():
        return {}
    with path.open("r", encoding="utf-8") as fh:
        return json.load(fh)


def write_json(path: Path, data: Dict[str, Any]):
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as fh:
        json.dump(data, fh, indent=2, ensure_ascii=False)


def safe_write_text(path: Path, content: str):
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as fh:
        fh.write(content)


def load_requirements(path: Path = None):
    path = path or Config.REQUIREMENTS_FILE
    if not path.exists():
        return []
    with path.open("r", encoding="utf-8") as fh:
        lines = [l.strip() for l in fh if l.strip() and not l.strip().startswith("#")]
    return lines
