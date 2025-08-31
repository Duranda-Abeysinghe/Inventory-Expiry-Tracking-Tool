import csv

class ExpiryAnalytics:
    def __init__(self):
        self.expired_log = {}

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
