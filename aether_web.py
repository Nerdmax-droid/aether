import requests
from flask import Flask, render_template_string, request

app = Flask(__name__)

def get_wikipedia_summary(topic):
    url = f"https://en.wikipedia.org/api/rest_v1/page/summary/{topic}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data.get('extract', "No summary available.")
    else:
        return "Sorry, I couldn't find that topic."

# Futuristic HTML template
html_template = """
<!DOCTYPE html>
<html>
<head>
    <title>Aether AI</title>
    <style>
        body {
            background-color: #0a0a0a;
            color: #00ffcc;
            font-family: 'Courier New', monospace;
            text-align: center;
        }
        h1 {
            font-size: 50px;
            color: #00ffff;
            text-shadow: 0 0 20px #00ffff;
        }
        input {
            width: 50%;
            padding: 10px;
            font-size: 18px;
            background: #111;
            color: #00ffcc;
            border: 2px solid #00ffcc;
        }
        button {
            padding: 10px 20px;
            font-size: 18px;
            background: #00ffcc;
            border: none;
            cursor: pointer;
        }
        .answer {
            margin-top: 20px;
            font-size: 20px;
            color: #ffffff;
        }
    </style>
</head>
<body>
    <h1>⚡ AETHER ⚡</h1>
    <form method="POST">
        <input type="text" name="topic" placeholder="Ask Aether anything...">
        <button type="submit">Ask</button>
    </form>
    {% if answer %}
        <div class="answer">
            <h2>Aether says:</h2>
            <p>{{ answer }}</p>
        </div>
    {% endif %}
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def home():
    answer = None
    if request.method == "POST":
        topic = request.form.get("topic")
        answer = get_wikipedia_summary(topic)
    return render_template_string(html_template, answer=answer)

if __name__ == "__main__":
    app.run(debug=True)
