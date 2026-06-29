"""
Initializer and entrypoint for Build Your Habit Premium.
Provides simple CLI to initialize project structure and run a placeholder app.
"""
import argparse
import sys
from pathlib import Path

from config import Config, ensure_dirs
from utils import setup_logging, safe_write_text, load_requirements
from chatgpt import query_chatgpt

DEFAULT_REQUIREMENTS = """# Tambahkan dependensi Python proyek di sini
# Contoh:
# fastapi==0.95.0
# uvicorn[standard]==0.22.0
"""

SAMPLE_APP = """"""Simple placeholder app for Build Your Habit Premium."""
def run():
    print('Running Build Your Habit Premium (placeholder).')

if __name__ == '__main__':
    run()
"""


def create_default_files():
    # Ensure directories
    ensure_dirs()
    # requirements.txt
    if not Config.REQUIREMENTS_FILE.exists():
        safe_write_text(Config.REQUIREMENTS_FILE, DEFAULT_REQUIREMENTS)
    # src/__init__.py and sample app
    app_file = Config.SRC_DIR / "app.py"
    init_file = Config.SRC_DIR / "__init__.py"
    if not init_file.exists():
        safe_write_text(init_file, "# src package")
    if not app_file.exists():
        safe_write_text(app_file, SAMPLE_APP)
    print("Project initialized. Directories and example files created.")


def show_status():
    print(f"{Config.APP_NAME} (v{Config.VERSION})")
    print("Project directories:")
    for d in (Config.DATA_DIR, Config.SRC_DIR, Config.TESTS_DIR):
        print(f" - {d} {'(exists)' if d.exists() else '(missing)'}")
    reqs = load_requirements()
    print(f"requirements.txt: {len(reqs)} packages listed")


def main(argv=None):
    setup_logging()
    parser = argparse.ArgumentParser(prog="build-your-habit-premium")
    parser.add_argument("--init", action="store_true", help="Initialize project structure and example files")
    parser.add_argument("--status", action="store_true", help="Show project status")
    parser.add_argument("--chat", "-c", nargs="+", help="Kirim prompt ke ChatGPT dan tampilkan hasilnya")
    args = parser.parse_args(argv or sys.argv[1:])
    if args.init:
        create_default_files()
        return
    if args.status:
        show_status()
        return
    if args.chat:
        prompt = " ".join(args.chat)
        try:
            answer = query_chatgpt(prompt)
            print("ChatGPT response:\n")
            print(answer)
        except Exception as e:
            print("Gagal memanggil ChatGPT:", e)
        return
    parser.print_help()


if __name__ == "__main__":
    main()
