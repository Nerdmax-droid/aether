import os
import pyfiglet
from flask import Flask, render_template_string, request
from transformers import pipeline

app = Flask(__name__)

# Use a free Hugging Face model (no API key required)
generator = pipeline("text-generation", model="mistralai/Mistral-7B-Instruct")

def get_ai_answer(question):
    lower_q = question.lower()
    if "origin" in lower_q or "creator" in lower_q or "who made you" in lower_q:
        return "I was created by Zach, and my name is Aether — your futuristic AI companion."
    try:
        result = generator(question, max_length=150, temperature=0.7)
        return result[0]["generated_text"]
    except Exception:
        return "⚠️ Aether is low on energy. Please try again later

# Artistic bubble letters heading
banner = pyfiglet.figlet_format("AETHER", font="bubble")

# HTML template with blue/white futuristic theme
html_template = """
<!DOCTYPE html>
<html>
<head>
    <title>Aether AI</title>
    <style>
        body {
            margin: 0;
            background: linear-gradient(135deg, #0a0f1f, #1a2a4f);
            color: #e0f7ff;
            font-family: 'Courier New', monospace;
            text-align: center;
        }
        pre.banner {
            font-size: 22px;
            color: #66ccff;
            text-shadow: 0 0 15px #99ddff, 0 0 30px #3399ff;
            margin-top: 20px;
        }
        input {
            width: 50%;
            padding: 12px;
            font-size: 18px;
            background: #112244;
            color: #e0f7ff;
            border: 2px solid #66ccff;
            border-radius: 8px;
        }
        button {
            padding: 12px 24px;
            font-size: 18px;
            background: #3399ff;
            color: white;
            border: none;
            border-radius: 8px;
            cursor: pointer;
            box-shadow: 0 0 10px #66ccff;
        }
        button:hover {
            background: #66ccff;
        }
        .answer {
            margin-top: 25px;
            font-size: 20px;
            color: #ffffff;
            background: rgba(51, 153, 255, 0.2);
            display: inline-block;
            padding: 15px;
            border-radius: 10px;
            box-shadow: 0 0 15px #3399ff;
        }
    </style>
</head>
<body>
    <pre class="banner">""" + banner + """</pre>
    <form method="POST">
        <input type="text" name="topic" placeholder="Ask Aether anything...">
        <button type="submit">Ask</button>
    </form>
    {% if gpt_answer %}
        <div class="answer">
            <h2>Aether says:</h2>
            <p>{{ gpt_answer }}</p>
        </div>
    {% endif %}
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def home():
    gpt_answer = None
    if request.method == "POST":
        topic = request.form.get("topic")
        gpt_answer = get_chatgpt_answer(topic)
    return render_template_string(html_template, gpt_answer=gpt_answer)

if __name__ == "__main__":
    app.run(debug=True)
