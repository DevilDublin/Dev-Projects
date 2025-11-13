from flask import Flask, request, render_template
import re

app = Flask(__name__)

ACTION_KEYWORDS = [
    "investigate", "look into", "fix", "check", "clear", "resolve",
    "test", "triple-check", "update", "adjust", "send", "review",
    "prepare", "schedule", "enable", "configure", "improve",
]

REQUEST_TRIGGERS = [
    "could you", "can you", "please can you", "please could you",
    "we need to", "we need you to", "i need you to", "i need to",
    "if possible could you", "if possible can you",
]

LINKING_PREFIXES = [
    "before that,", "before that ,", "before that",
    "first,", "first of all,", "also,", "also ", "lastly,", "lastly ",
]

SKIP_PREFIXES_SENTENCE = [
    "hi ", "hello ", "dear ",
]

SKIP_PREFIXES_ACTION = [
    "we noticed", "we tested", "we received",
    "another thing", "this fixed", "this creates",
    "this is", "on ios", "a few customers",
    "sorry for the long email", "hope you’re keeping well",
    "hope you're keeping well", "i wanted to send over a detailed update",
]

CLAUSE_BREAKERS = [
    " and ", " because ", " which ", " that ", " as ", " so ",
    " but ", " while ", " although ", " though ",
]


def get_email_text(form):
    return (
        form.get("email_text")
        or form.get("email")
        or form.get("body")
        or form.get("message")
        or ""
    )


def extract_summary(text: str) -> str:
    text = text.strip()
    if not text:
        return "No summary available."

    sentences = re.split(r"(?<=[.!?])\s+", text)
    for s in sentences:
        s_clean = s.strip()
        if not s_clean:
            continue
        lower = s_clean.lower()
        if any(lower.startswith(p) for p in SKIP_PREFIXES_SENTENCE):
            continue
        if len(s_clean) > 140:
            s_clean = s_clean[:140].rstrip() + "…"
        return s_clean

    return "No summary available."


def find_trigger(lower: str):
    best_idx = None
    best_trig = None
    for trig in REQUEST_TRIGGERS:
        idx = lower.find(trig)
        if idx == -1:
            continue
        if idx > 60:
            continue
        if best_idx is None or idx < best_idx:
            best_idx = idx
            best_trig = trig
    return best_idx, best_trig


def is_action_sentence(sentence: str) -> bool:
    lower = sentence.lower().strip()

    if any(lower.startswith(p) for p in SKIP_PREFIXES_ACTION):
        return False

    idx, trig = find_trigger(lower)
    if trig is not None:
        return True

    for verb in ACTION_KEYWORDS:
        if lower.startswith(verb + " "):
            return True

    return False


def trim_to_first_clause(s: str) -> str:
    lower = s.lower()
    cut = len(s)
    for br in CLAUSE_BREAKERS:
        idx = lower.find(br)
        if idx != -1 and idx < cut:
            cut = idx
    return s[:cut].strip(" ,;:-")


def clean_into_task(sentence: str) -> str:
    s = sentence.strip()
    lower = s.lower()

    # drop linking phrases like "Before that,"
    for pref in LINKING_PREFIXES:
        if lower.startswith(pref):
            s = s[len(pref):].lstrip(" ,.-")
            lower = s.lower()
            break

    # drop soft connectors
    for start in ["but ", "and ", "so "]:
        if lower.startswith(start):
            s = s[len(start):]
            lower = s.lower()

    # cut off polite/request wrapper at the start of the clause
    idx, trig = find_trigger(lower)
    if trig is not None:
        s = sentence[idx + len(trig):].lstrip(" ,.-")
        lower = s.lower()

    for lead in ["we need you to", "we need to", "i need you to", "i need to"]:
        if lower.startswith(lead):
            s = s[len(lead):].lstrip(" ,.-")
            lower = s.lower()
            break

    # strip "please" if it still survives
    if lower.startswith("please "):
        s = s[7:].lstrip(" ,.-")
        lower = s.lower()

    # weird edge case from earlier runs: "U to update..."
    if lower.startswith("u to "):
        s = s[4:].lstrip(" ,.-")
        lower = s.lower()

    s = trim_to_first_clause(s).strip()
    if not s:
        return ""

    words = s.split()
    if not words:
        return ""

    # drop obviously non-tasky starts
    if words[0].lower() in ["we", "i", "this", "another", "maybe"]:
        return ""

    # capitalise and shorten
    s = s[0].upper() + s[1:]
    if len(words) > 18:
        s = " ".join(words[:18]) + "…"

    # remove trailing punctuation like "?", "." etc.
    s = s.rstrip(" .!?")

    return s


def extract_actions(text: str):
    text = text.strip()
    if not text:
        return []

    flattened = " ".join(line.strip() for line in text.splitlines())
    sentences = re.split(r"(?<=[.!?])\s+", flattened)

    actions = []
    for sentence in sentences:
        raw = sentence.strip()
        if not raw:
            continue
        if not is_action_sentence(raw):
            continue

        cleaned = clean_into_task(raw)
        if cleaned:
            actions.append(cleaned)

    seen = set()
    result = []
    for a in actions:
        if a not in seen:
            seen.add(a)
            result.append(a)

    return result[:10]


@app.route("/", methods=["GET", "POST"])
def index():
    summary = ""
    actions = []

    if request.method == "POST":
        email_text = get_email_text(request.form)
        summary = extract_summary(email_text)
        actions = extract_actions(email_text)

    return render_template("index.html", summary=summary, actions=actions)


if __name__ == "__main__":
    app.run(debug=True, port=5000)
