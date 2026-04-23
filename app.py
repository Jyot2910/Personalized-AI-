import os
from dotenv import load_dotenv
from openai import OpenAI

# ---------------- Environment Setup ----------------
load_dotenv()

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

if not OPENROUTER_API_KEY:
    raise ValueError("OPENROUTER_API_KEY not found in .env file")

# ---------------- OpenRouter Client ----------------
client = OpenAI(
    api_key=OPENROUTER_API_KEY,
    base_url="https://openrouter.ai/api/v1"
)

# ---------------- Rashi AI Brain ----------------
def get_answer(question: str) -> str:
    try:
        response = client.chat.completions.create(
            model="openai/gpt-3.5-turbo",
            messages=[
                {
                    "role": "system",
                    "content": (
                        "You are Rashi, a polite, friendly female AI assistant. "
                        "Keep responses concise and conversational (2-3 sentences max for voice output)."
                    )
                },
                {
                    "role": "user",
                    "content": question
                }
            ],
            max_tokens=150,
            temperature=0.7
        )

        return response.choices[0].message.content.strip()

    except Exception as e:
        print(f"Error from OpenRouter API: {e}")
        return "I'm having trouble connecting right now. Please try again."


def test_connection():
    """Test if OpenRouter API is working"""
    try:
        response = get_answer("Say hello in one sentence")
        print("✓ OpenRouter API connected successfully!")
        print(f"Test response: {response}")
        return True   # ✅ CRITICAL FIX
    except Exception as e:
        print(f"✗ OpenRouter API connection failed: {e}")
        return False
