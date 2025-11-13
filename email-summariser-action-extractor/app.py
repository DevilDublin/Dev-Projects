from flask import Flask, render_template, request

app = Flask(__name__)


def simple_summarise(text: str) -> str:
  lines = [line.strip() for line in text.splitlines() if line.strip()]
  if not lines:
    return ""
  if len(lines) == 1:
    return lines[0]
  return lines[0] + (" ..." if len(lines) > 1 else "")


def extract_actions(text: str):
  actions = []
  for line in text.splitlines():
    stripped = line.strip()
    if not stripped:
      continue
    lowered = stripped.lower()
    if lowered.startswith(("please", "can you", "could you", "i need you to")):
      actions.append(stripped)
  return actions


@app.route("/", methods=["GET", "POST"])
def index():
  summary = ""
  actions = []
  original = ""
  if request.method == "POST":
    original = request.form.get("body", "")
    summary = simple_summarise(original)
    actions = extract_actions(original)
  return render_template("index.html", summary=summary, actions=actions, original=original)


if __name__ == "__main__":
  app.run(debug=True)
