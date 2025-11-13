import csv
from pathlib import Path


def load_inventory():
    csv_path = Path(__file__).with_name("inventory.csv")

    rows = []
    with csv_path.open(newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            name = row.get("Item") or row.get("item") or row.get("name")
            qty_raw = row.get("Qty") or row.get("qty") or row.get("quantity")
            usage_raw = (
                row.get("DailyUsage")
                or row.get("daily_usage")
                or row.get("Daily usage")
            )

            if not name:
                continue

            try:
                qty = int(qty_raw)
            except (TypeError, ValueError):
                qty = 0

            try:
                usage = float(usage_raw)
            except (TypeError, ValueError):
                usage = 0.0

            rows.append({"name": name, "qty": qty, "usage": usage})

    return rows


def classify_item(qty, usage):
    if usage <= 0:
        return float("inf"), "No usage data", None

    days_left = qty / usage

    if days_left < 3:
        status = "Critical"
        warning = "Running critically low"
    elif days_left < 7:
        status = "Low"
        warning = "Should be reordered soon"
    else:
        status = "OK"
        warning = None

    return days_left, status, warning


def format_table(rows):
    header = (
        f"{'Item':<24}"
        f"{'Qty':<7}"
        f"{'Daily usage':<14}"
        f"{'Days left':<11}"
        f"{'Status':<12}"
    )
    separator = "-" * len(header)

    lines = [header, separator]

    warnings = []

    for row in rows:
        name = row["name"]
        qty = row["qty"]
        usage = row["usage"]

        days_left, status, warning = classify_item(qty, usage)

        if usage > 0:
            usage_str = f"{usage:.1f}".rstrip("0").rstrip(".")
        else:
            usage_str = "-"

        if days_left == float("inf"):
            days_str = "-"
        else:
            days_str = f"{days_left:.1f}".rstrip("0").rstrip(".")

        line = (
            f"{name:<24}"
            f"{qty:<7}"
            f"{usage_str:<14}"
            f"{days_str:<11}"
            f"{status:<12}"
        )
        lines.append(line)

        if warning:
            warnings.append(f"- {name}: {warning}")

    return lines, warnings


def main():
    print()
    print(" SMART INVENTORY TRACKER — CONSOLE VIEW")
    print(" -------------------------------------")
    print()

    rows = load_inventory()
    lines, warnings = format_table(rows)

    for line in lines:
        print(line)

    if warnings:
        print()
        print("Warnings:")
        for w in warnings:
            print(w)
    else:
        print()
        print("No low-stock warnings.")


if __name__ == "__main__":
    main()
