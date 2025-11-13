from flask import Flask, render_template_string, request
from password_auditor import score_password, suggest_stronger

app = Flask(__name__)

TEMPLATE = '''
<!doctype html>
<html>
<head>
  <meta charset="utf-8">
  <title>Password Strength Auditor</title>
</head>
<body>
  <h1>Password Strength Auditor</h1>
  <form method="post">
    <input type="password" name="password" placeholder="Enter password" required>
    <button type="submit">Check</button>
  </form>

  {% if result %}
    <h2>Result</h2>
    <p><strong>Strength:</strong> {{ result.strength }} (score {{ result.score }})</p>
    {% if result.reasons %}
      <h3>Issues</h3>
      <ul>
        {% for r in result.reasons %}
          <li>{{ r }}</li>
        {% endfor %}
      </ul>
    {% endif %}
    <h3>Suggested stronger password</h3>
    <p>{{ result.suggestion }}</p>
  {% endif %}
</body>
</html>
'''

@app.route("/", methods=["GET", "POST"])
def index():
  result = None
  if request.method == "POST":
    pw = request.form.get("password", "")
    strength, reasons, score = score_password(pw)
    suggestion = suggest_stronger(pw)
    result = {
      "strength": strength,
      "reasons": reasons,
      "score": score,
      "suggestion": suggestion
    }
  return render_template_string(TEMPLATE, result=result)


if __name__ == "__main__":
  app.run(debug=True)
