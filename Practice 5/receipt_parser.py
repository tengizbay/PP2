import re
import json

# Read receipt
with open("raw.txt", "r", encoding="utf-8") as f:
    text = f.read()

# 1. Extract all prices

price_pattern = r"\d{1,3}(?:\s\d{3})*,\d{2}"
prices_raw = re.findall(price_pattern, text)

prices = []
for p in prices_raw:
    clean = p.replace(" ", "").replace(",", ".")
    prices.append(float(clean))

# 2. Extract product names

product_pattern = r"\d+\.\s*\n([^\n]+)"
products = re.findall(product_pattern, text)

# 3. Calculate total amount

total_calculated = sum(prices)

# 4. Extract date and time

datetime_pattern = r"\d{2}\.\d{2}\.\d{4}\s\d{2}:\d{2}:\d{2}"
datetime_match = re.search(datetime_pattern, text)

date = None
time = None

if datetime_match:
    date, time = datetime_match.group().split()


# 5. Find payment method

payment_pattern = r"(Банковская карта|Наличные)"
payment_match = re.search(payment_pattern, text)

payment_method = payment_match.group() if payment_match else None


# 6. Structured Output

data = {
    "products": products,
    "prices": prices,
    "calculated_total": total_calculated,
    "date": date,
    "time": time,
    "payment_method": payment_method
}

print(json.dumps(data, indent=4, ensure_ascii=False))