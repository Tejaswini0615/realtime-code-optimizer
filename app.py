from flask import Flask, request, jsonify
import google.generativeai as genai
import os
import time

# ✅ Set up Gemini API key from Environment Variable
api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise ValueError("GEMINI_API_KEY is not set. Please export it before running.")

genai.configure(api_key=api_key)

app = Flask(__name__)

@app.route('/analyze', methods=['POST'])
def analyze_code():
    code_snippet = request.json.get('code')

    if not code_snippet:
        return jsonify({"error": "No code provided"}), 400

    prompt = f"""
    Analyze the following Python code, suggest performance improvements, and provide only the optimized version of the code.

    Code:

    {code_snippet}

    Optimized Code:
    """

    model = genai.GenerativeModel("gemini-1.5-flash")

    try:
        response = model.generate_content(prompt)
        optimized_code = response.text

        return jsonify({
            'ai_suggestion': optimized_code
        })

    except Exception as e:
        return jsonify({'error': str(e)}), 500


if __name__ == "__main__":
    app.run(port=5000)
