from datetime import datetime
import heapq
from collections import deque
import csv
import json
import os


class Product:
    def __init__(self, name, quantity, expiry_date):
        self.name = name
        self.quantity = quantity
        self.expiry_date = datetime.strptime(expiry_date, "%Y-%m-%d").date()
        self.added_time = datetime.now()  

    def days_until_expiry(self):
        today = datetime.today().date()
        return (self.expiry_date - today).days

    def __lt__(self, other):
        return self.expiry_date < other.expiry_date

    def __str__(self):
        days = self.days_until_expiry()
        status = "Expired" if days < 0 else f"Near expiry ({days} days)" if days <= 3 else "Valid"
        return f"{self.name} | Qty: {self.quantity} | Expiry: {self.expiry_date} | Status: {status}"


class InventoryExpiryTracker:
    def __init__(self):
        self.expiry_heap = []      
        self.add_order_list = []   
        self.stock_queue = deque() 
        self.expired_log = {}      
        self.threshold = 3         
        self.load_inventory()      
        self.show_alerts()         

    def add_product(self, product):
        heapq.heappush(self.expiry_heap, product)
        self.add_order_list.append(product)
        self.stock_queue.append(f"🔥 Added: {product.name}")
        self.save_inventory()

    def remove_product(self):
        if self.expiry_heap:
            removed = heapq.heappop(self.expiry_heap)
            if removed in self.add_order_list:
                self.add_order_list.remove(removed)

            if removed in self.stock_queue:
                self.stock_queue.remove(removed)
            if removed.days_until_expiry() < 0:
                if removed.name not in self.expired_log:
                    self.expired_log[removed.name] = 0
                self.expired_log[removed.name] += removed.quantity

            self.stock_queue.append(f"❌ Removed: {removed.name}")  
            self.save_inventory()
            return removed
        return None

  
    def update_product(self, name, new_qty):
        for prod in self.expiry_heap:
            if prod.name == name:
                prod.quantity = new_qty
                self.stock_queue.append(f"Updated: {prod.name} to {new_qty}")
                heapq.heapify(self.expiry_heap)
                self.save_inventory()
                return prod
        return None

    
    def show_products(self):
        print("\n---- Inventory (Order Added) ----")
        if not self.add_order_list:
            print("No products in inventory.")
        for prod in self.add_order_list:
            print(prod)

    
    def show_sorted_by_expiry(self):
        print("\n---- Products Sorted by Expiry ----")
        for prod in sorted(self.expiry_heap, key=lambda x: x.expiry_date):
            print(prod)

   
    def show_alerts(self):
        print("\n---- Expiry Alerts / Reminder ----")
        alerts_exist = False
        for prod in self.expiry_heap:
            days = prod.days_until_expiry()
            if days < 0 or days <= self.threshold:
                print(prod)
                alerts_exist = True
        if not alerts_exist:
            print("No expired or near-expiry products.")

    def show_stock_log(self):
        print("\n---- Stock Operations ----")
        for log in self.stock_queue:
            print(log)

    def export_alerts_csv(self, filename="expiry_alerts.csv"):
        with open(filename, mode="w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Product Name", "Quantity", "Expiry Date", "Status"])
            for prod in self.expiry_heap:
                days = prod.days_until_expiry()
                if days < 0 or days <= self.threshold:
                    status = "Expired" if days < 0 else f"Near expiry ({days} days)"
                    writer.writerow([prod.name, prod.quantity, prod.expiry_date, status])
        print(f"Alerts exported to {filename}")


    def show_expiry_analytics(self):
        print("\n---- Expiry Analytics / Loss Report ----")
        if not self.expired_log:
            print("No expired items recorded.")
            return
        
        total_expired_qty = sum(self.expired_log.values())
        most_expired_item = max(self.expired_log, key=self.expired_log.get)
        
        print(f"Total expired quantity: {total_expired_qty}")
        print(f"Most frequently expired product: {most_expired_item} ({self.expired_log[most_expired_item]} units)")
        print("\nDetailed expired items:")
        for name, qty in self.expired_log.items():
            print(f"{name}: {qty} units")

    def export_expiry_analytics_csv(self, filename="expiry_analytics.csv"):
        with open(filename, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["Product Name", "Expired Quantity"])
            for name, qty in self.expired_log.items():
                writer.writerow([name, qty])
        print(f"Expiry analytics exported to {filename}")

  
    def save_inventory(self, filename="inventory.json"):
        data = []
        for prod in self.add_order_list:  
            data.append({
                "name": prod.name,
                "quantity": prod.quantity,
                "expiry_date": str(prod.expiry_date)
            })
        with open(filename, "w") as f:
            json.dump(data, f)

    def load_inventory(self, filename="inventory.json"):
        if os.path.exists(filename):
            with open(filename, "r") as f:
                data = json.load(f)
                for item in data:
                    prod = Product(item["name"], item["quantity"], item["expiry_date"])
                    self.expiry_heap.append(prod)
                    self.add_order_list.append(prod)
            heapq.heapify(self.expiry_heap)


def main():
    tool = InventoryExpiryTracker()
    print("=== Inventory Expiry Tracker Tool ===")
    while True:
        print("\n1. Add Product\n2. Remove Next Expiring Product\n3. Update Product Quantity\n"
              "4. Show All Products (Order Added)\n5. Show Recent Operations\n6. Export Alerts to CSV\n"
              "7. Show Products Sorted by Expiry\n8. Show Expiry Analytics\n9. Export Expiry Analytics CSV\n10. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Product Name: ")
            qty = int(input("Quantity: "))
            expiry = input("Expiry Date (YYYY-MM-DD): ")
            tool.add_product(Product(name, qty, expiry))
        elif choice == "2":
            removed = tool.remove_product()
            print(f"Removed: {removed.name}" if removed else "No products to remove.")
        elif choice == "3":
            name = input("Product Name to Update: ")
            qty = int(input("New Quantity: "))
            updated = tool.update_product(name, qty)
            print(f"Updated: {updated}" if updated else "Product not found.")
        elif choice == "4":
            tool.show_products()
        elif choice == "5":
            tool.show_stock_log()
        elif choice == "6":
            tool.export_alerts_csv()
        elif choice == "7":
            tool.show_sorted_by_expiry()
        elif choice == "8":
            tool.show_expiry_analytics()
        elif choice == "9":
            tool.export_expiry_analytics_csv()
        elif choice == "10":
            print("Exiting Tool...")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
