import google.generativeai as genai
import os

# ✅ Load API key from environment variable
API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    raise ValueError("❌ Error: Missing GEMINI_API_KEY. Please set it in the environment.")

genai.configure(api_key=API_KEY)
model = genai.GenerativeModel("gemini-pro")

def suggest_optimization(code_snippet):
    prompt = f"Analyze and optimize this Python code:\n\n{code_snippet}"
    response = model.generate_content(prompt)

    if response and response.text:
        return response.text.strip()
    return "No optimization suggestion available."
