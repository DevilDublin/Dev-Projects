from flask import Flask, render_template_string, request
from password_auditor import score_password, generate_suggestions

app = Flask(__name__)

TEMPLATE = """
<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <title>Password Strength Auditor</title>
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&display=swap" rel="stylesheet">
  <style>
    * { box-sizing: border-box; }
    body {
      margin: 0;
      min-height: 100vh;
      display: flex;
      align-items: center;
      justify-content: center;
      background: radial-gradient(circle at top, #151b2b 0, #050711 55%);
      font-family: "Inter", system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
      color: #f5f5f5;
    }
    .wrapper {
      width: 100%;
      max-width: 520px;
      padding: 24px;
    }
    .card {
      background: rgba(9, 13, 24, 0.96);
      border-radius: 18px;
      padding: 22px 24px 20px;
      border: 1px solid #252b3c;
      box-shadow: 0 18px 45px rgba(0, 0, 0, 0.45);
    }
    h1 {
      font-size: 22px;
      margin: 0 0 4px;
    }
    .subtitle {
      font-size: 13px;
      color: #a2a7bb;
      margin-bottom: 18px;
    }
    label {
      font-size: 13px;
      display: block;
      margin-bottom: 6px;
    }
    input[type="password"] {
      width: 100%;
      padding: 9px 11px;
      border-radius: 10px;
      border: 1px solid #32384a;
      background: #070915;
      color: #f5f5f5;
      font-size: 13px;
      outline: none;
    }
    input[type="password"]:focus {
      border-color: #39ff14;
      box-shadow: 0 0 0 1px rgba(57, 255, 20, 0.25);
    }
    button {
      margin-top: 10px;
      border-radius: 999px;
      border: none;
      padding: 8px 18px;
      font-size: 13px;
      font-weight: 500;
      cursor: pointer;
      background: #39ff14;
      color: #02040a;
    }
    button:hover { filter: brightness(1.08); }
    .result {
      margin-top: 18px;
      padding-top: 14px;
      border-top: 1px solid #242a3a;
      font-size: 13px;
    }
    .badge {
      display: inline-flex;
      align-items: centre;
      gap: 6px;
      padding: 3px 10px 4px;
      border-radius: 999px;
      font-size: 11px;
      background: rgba(57, 255, 20, 0.08);
      color: #8eff6a;
    }
    .issues {
      margin: 10px 0 0;
      padding-left: 18px;
      color: #cfd3e6;
    }
    .hint-title {
      margin-top: 12px;
      font-size: 12px;
      color: #a2a7bb;
    }
    .suggestions-row {
      display: flex;
      flex-wrap: wrap;
      gap: 8px;
      margin-top: 6px;
    }
    .suggestion-chip {
      padding: 6px 10px;
      border-radius: 999px;
      background: #050815;
      border: 1px solid #343b50;
      font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas,
                   "Liberation Mono", "Courier New", monospace;
      font-size: 12px;
      color: #d4d8ea;
    }
    .muted {
      color: #8f95ad;
      font-size: 11px;
      margin-top: 10px;
    }
  </style>
</head>
<body>
  <div class="wrapper">
    <div class="card">
      <h1>Password Strength Auditor</h1>
      <p class="subtitle">Check how strong a password is and see what’s weakening it.</p>

      <form method="post">
        <label for="pw">Password</label>
        <input id="pw" type="password" name="password"
               placeholder="Enter a password to check" required autofocus>
        <button type="submit">Audit password</button>
      </form>

      {% if result %}
      <div class="result">
        <div class="badge">
          <span>Strength: <strong>{{ result.strength }}</strong></span>
          <span>· score {{ result.score }}</span>
        </div>

        {% if result.reasons %}
        <ul class="issues">
          {% for r in result.reasons %}
          <li>{{ r }}</li>
          {% endfor %}
        </ul>
        {% endif %}

        {% if result.suggestions %}
        <p class="hint-title">Stronger variants you could use</p>
        <div class="suggestions-row">
          {% for s in result.suggestions %}
          <span class="suggestion-chip">{{ s }}</span>
          {% endfor %}
        </div>
        {% endif %}
      </div>
      {% endif %}

      <p class="muted">Everything runs locally – nothing is sent anywhere.</p>
    </div>
  </div>
</body>
</html>
"""


@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    if request.method == "POST":
        pw = request.form.get("password", "")
        strength, reasons, score = score_password(pw)
        suggestions = generate_suggestions(pw)
        result = {
            "strength": strength,
            "reasons": reasons,
            "score": score,
            "suggestions": suggestions,
        }
    return render_template_string(TEMPLATE, result=result)


if __name__ == "__main__":
    app.run(debug=True)
