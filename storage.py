import json

def save_inventory(add_order_list, filename="inventory.json"):
    data = []
    for prod in add_order_list:
        data.append({
            "name": prod.name,
            "quantity": prod.quantity,
            "expiry_date": str(prod.expiry_date)
        })
    with open(filename, "w") as f:
        json.dump(data, f)
