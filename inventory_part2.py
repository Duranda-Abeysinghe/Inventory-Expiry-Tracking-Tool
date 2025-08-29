from storage import save_inventory, load_inventory
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
