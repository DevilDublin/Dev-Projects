import re
from typing import List, Tuple, Set


def load_common_passwords(filename: str = "common_passwords.txt") -> Set[str]:
    try:
        with open(filename, "r", encoding="utf-8") as f:
            return {line.strip() for line in f if line.strip()}
    except FileNotFoundError:
        return set()


COMMON_PASSWORDS: Set[str] = load_common_passwords()


def score_password(pw: str) -> Tuple[str, List[str], int]:
    reasons: List[str] = []
    score = 0
    length = len(pw)

    # Length
    if length < 8:
        reasons.append("Too short (fewer than 8 characters).")
    elif length < 12:
        score += 1
    else:
        score += 2

    # Variety
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

    # Patterns
    if pw.lower() in COMMON_PASSWORDS:
        reasons.append("Matches a very common password.")
        score -= 2

    if re.search(r"(1234|0000|1111|abcd)", pw.lower()):
        reasons.append("Contains an easy guess sequence (for example 1234).")
        score -= 1

    if re.search(r"(.)\\1{2,}", pw):
        reasons.append("Contains repeated characters (for example aaa, 111).")
        score -= 1

    # Final label
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


def _base_upgrade(pw: str) -> str:
    """Apply a minimal upgrade to meet decent standards."""
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


def generate_suggestions(pw: str) -> List[str]:
    """
    Return a small set of stronger variants based on the original password.
    These stay recognisable so they are still memorable.
    """
    base = _base_upgrade(pw)
    variants = {base}

    # Variant 1 – prefix plus base
    variants.add("!" + base + "7")

    # Variant 2 – simple leet-style swap
    leet = (
        base.replace("a", "@")
        .replace("A", "@")
        .replace("o", "0")
        .replace("i", "1")
        .replace("s", "$")
    )
    variants.add(leet)

    # Variant 3 – add year-style suffix
    variants.add(base + "24")

    # Keep it small and stable
    ordered = list(variants)
    return ordered[:3]


def main() -> None:
    print("=== Password Strength Auditor ===")
    pw = input("Enter a password to check: ")
    strength, reasons, score = score_password(pw)

    print(f"\nStrength: {strength} (score: {score})")
    if reasons:
        print("\nIssues found:")
        for r in reasons:
            print(f" - {r}")

    if strength in ("Very Weak", "Weak", "Medium"):
        print("\nSuggested stronger options:")
        for s in generate_suggestions(pw):
            print(f" - {s}")


if __name__ == "__main__":
    main()
