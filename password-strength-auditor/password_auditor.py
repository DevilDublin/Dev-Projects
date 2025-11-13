import re

def load_common_passwords(filename="common_passwords.txt"):
  try:
    with open(filename, "r", encoding="utf-8") as f:
      return {line.strip() for line in f if line.strip()}
  except FileNotFoundError:
    return set()

COMMON_PASSWORDS = load_common_passwords()


def score_password(pw: str):
  reasons = []
  score = 0
  length = len(pw)

  if length < 8:
    reasons.append("Too short (less than 8 characters).")
  elif length < 12:
    score += 1
  else:
    score += 2

  has_lower = any(c.islower() for c in pw)
  has_upper = any(c.isupper() for c in pw)
  has_digit = any(c.isdigit() for c in pw)
  has_symbol = any(not c.isalnum() for c in pw)
  classes = sum([has_lower, has_upper, has_digit, has_symbol])

  if classes <= 1:
    reasons.append("Not enough character variety.")
  elif classes == 2:
    score += 1
  else:
    score += 2

  if pw.lower() in COMMON_PASSWORDS:
    reasons.append("This is a very common password.")
    score -= 2

  if re.search(r"(1234|0000|1111|abcd)", pw.lower()):
    reasons.append("Contains an easily guessable sequence.")
    score -= 1

  if re.search(r"(.)\1{2,}", pw):
    reasons.append("Contains repeated characters (e.g. aaa, 111).")
    score -= 1

  if score <= 0:
    strength = "Very Weak"
  elif score == 1:
    strength = "Weak"
  elif score == 2:
    strength = "Medium"
  elif score == 3:
    strength = "Strong"
  else:
    strength = "Very Strong"

  return strength, reasons, score


def suggest_stronger(pw: str):
  suggestion = pw
  if len(suggestion) < 12:
    suggestion = suggestion + "!" * (12 - len(suggestion))
  if not any(c.isupper() for c in suggestion):
    suggestion += "A"
  if not any(c.isdigit() for c in suggestion):
    suggestion += "3"
  if not any(not c.isalnum() for c in suggestion):
    suggestion += "!"
  return suggestion


def main():
  print("=== Password Strength Auditor ===")
  pw = input("Enter a password to check: ")
  strength, reasons, score = score_password(pw)
  print(f"\nStrength: {strength} (score: {score})")
  if reasons:
    print("\nIssues:")
    for r in reasons:
      print(f"- {r}")
  if strength in ("Very Weak", "Weak", "Medium"):
    print("\nSuggested stronger password:")
    print(suggest_stronger(pw))


if __name__ == "__main__":
  main()
