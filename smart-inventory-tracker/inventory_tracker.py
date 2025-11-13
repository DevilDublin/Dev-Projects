import csv
from datetime import datetime, timedelta

DATA_FILE = "inventory.csv"


def load_inventory():
  items = []
  try:
    with open(DATA_FILE, newline="", encoding="utf-8") as f:
      reader = csv.DictReader(f)
      for row in reader:
        row["current_quantity"] = int(row.get("current_quantity", 0))
        row["average_daily_usage"] = float(row.get("average_daily_usage", 0))
        items.append(row)
  except FileNotFoundError:
    pass
  return items


def forecast_run_out(item):
  usage = item["average_daily_usage"]
  if usage <= 0:
    return None
  days = item["current_quantity"] / usage
  return datetime.today().date() + timedelta(days=int(days))


def main():
  print("=== Smart Inventory Tracker (demo) ===")
  items = load_inventory()
  if not items:
    print("No inventory.csv file found. Create one with columns: name,current_quantity,average_daily_usage")
    return

  for item in items:
    name = item.get("name", "Unknown")
    run_out_date = forecast_run_out(item)
    print(f"\nItem: {name}")
    print(f"Current quantity: {item['current_quantity']}")
    print(f"Average daily usage: {item['average_daily_usage']}")
    if run_out_date:
      print(f"Estimated run-out date: {run_out_date.isoformat()}")
      days_left = (run_out_date - datetime.today().date()).days
      if days_left <= 3:
        print("Warning: This item is likely to run out within 3 days.")
    else:
      print("Not enough data to forecast.")
  print("\nDemo complete.")


if __name__ == "__main__":
  main()
