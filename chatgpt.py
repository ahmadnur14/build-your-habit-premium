import os
from typing import Optional

from dotenv import load_dotenv
import openai

# Muat .env bila ada (development)
load_dotenv()

def init_openai(api_key: Optional[str] = None):
    key = api_key or os.getenv("OPENAI_API_KEY")
    if not key:
        raise RuntimeError(
            "OPENAI_API_KEY tidak ditemukan di environment. Buat file .env dan isi OPENAI_API_KEY atau set ENV variable."
        )
    openai.api_key = key

def query_chatgpt(prompt: str, system_prompt: Optional[str] = None, model: str = "gpt-3.5-turbo", temperature: float = 0.7) -> str:
    """
    Kirim prompt ke OpenAI Chat Completions dan kembalikan teks respons.
    """
    init_openai()
    messages = []
    if system_prompt:
        messages.append({"role": "system", "content": system_prompt})
    messages.append({"role": "user", "content": prompt})

    resp = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=temperature,
        max_tokens=800,
    )
    return resp.choices[0].message.content.strip()
