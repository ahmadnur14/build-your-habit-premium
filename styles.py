"""
Style constants / simple CSS for the project UI (or console styles).
This module centralizes visual/style settings so other parts of the app can import them.
"""
from dataclasses import dataclass

@dataclass(frozen=True)
class ConsoleColors:
    HEADER: str = "\033[95m"
    OKBLUE: str = "\033[94m"
    OKGREEN: str = "\033[92m"
    WARNING: str = "\033[93m"
    FAIL: str = "\033[91m"
    ENDC: str = "\033[0m"
    BOLD: str = "\033[1m"
    UNDERLINE: str = "\033[4m"

CONSOLE = ConsoleColors()

# Example CSS (useful if you add a web frontend later)
DEFAULT_CSS = """
:root{
  --primary:#4f46e5;
  --accent:#06b6d4;
  --bg:#0f172a;
  --card:#0b1220;
  --text:#e6eef8;
}
body{ background:var(--bg); color:var(--text); font-family:Inter, system-ui, -apple-system; }
.container{ max-width:900px; margin:32px auto; padding:24px; }
.card{ background:var(--card); padding:16px; border-radius:8px; box-shadow:0 4px 14px rgba(2,6,23,.6); }
"""
