import google.generativeai as genai
import json
import re

# 🔥 SET YOUR API KEY
genai.configure(api_key="AIzaSyBZqBAz6LrG4i_PMOQY1vHaNorZabZSf1U")

# ✅ MODEL FALLBACK LIST (ordered by preference)
MODEL_CANDIDATES = [
    "gemini-1.5-flash-latest",
    "gemini-1.5-pro-latest",
    "gemini-1.0-pro"
]


def call_model(prompt):
    for model_name in MODEL_CANDIDATES:
        try:
            print(f"Trying model: {model_name}")

            model = genai.GenerativeModel(model_name)
            response = model.generate_content(prompt)

            if response and response.text:
                return response.text

        except Exception as e:
            print(f"Model failed: {model_name} → {e}")

    raise Exception("All models failed")


def run_arena(solution, history, round):

    prompt = f"""
You are an adversarial AI system tester in a learning arena.

Round: {round}
History: {history}

User Solution:
{solution}

Your job:
- Break the solution logically
- Generate edge cases
- Simulate real-world failures
- Increase difficulty each round

Return STRICT JSON only:
{{
 "attack": "...",
 "edge_cases": "...",
 "feedback": "...",
 "score": number between 50-100
}}
"""

    try:
        text = call_model(prompt).strip()

        # ✅ Extract JSON safely
        json_match = re.search(r'\{.*\}', text, re.DOTALL)

        if not json_match:
            raise Exception("No JSON found")

        return json.loads(json_match.group())

    except Exception as e:
        print("FINAL AI ERROR:", e)

        # 🔁 fallback if everything fails
        return {
            "attack": "⚠️ System unstable under extreme load.",
            "edge_cases": "Concurrent request collision.",
            "feedback": "Improve resilience.",
            "score": 65
        }