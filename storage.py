import json, os
from product import Product

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

def load_inventory(expiry_heap, add_order_list, filename="inventory.json"):
    if os.path.exists(filename):
        import heapq
        with open(filename, "r") as f:
            data = json.load(f)
            for item in data:
                prod = Product(item["name"], item["quantity"], item["expiry_date"])
                expiry_heap.append(prod)
                add_order_list.append(prod)
        heapq.heapify(expiry_heap)
