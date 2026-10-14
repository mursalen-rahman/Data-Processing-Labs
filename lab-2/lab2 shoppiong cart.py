# Suggested data from exercise sheet
products = [
    {"name": "Notebook", "price": 120, "quantity": 3},
    {"name": "Pen", "price": 20, "quantity": 5},
    {"name": "USB Drive", "price": 850, "quantity": 2},
    {"name": "Mouse", "price": 650, "quantity": 1}
]

# Calculate total cost using a for loop
total_cost = 0
for item in products:
    item_total = item["price"] * item["quantity"]
    total_cost = total_cost + item_total

# Function to apply discount
def apply_discount(total):
    if total >= 2000:
        discount = total * 0.10  # 10% discount
        return total - discount
    else:
        return total

# Calculate final price
final_price = apply_discount(total_cost)

print("Original Total:", total_cost)
print("Final Price after discount check:", final_price)