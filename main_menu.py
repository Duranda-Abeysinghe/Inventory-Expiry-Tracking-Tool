from product import Product
from inventory import InventoryExpiryTracker

def main():
    tool = InventoryExpiryTracker()
    print("=== Inventory Expiry Tracker Tool ===")
    while True:
        print("\n1. Add Product\n2. Remove Next Expiring Product\n3. Update Product Quantity\n"
              "4. Show All Products (Order Added)\n5. Show Recent Operations\n6. Export Alerts to CSV\n7. Show Products Sorted by Expiry\n8. Show Expiry Analytics\n9. Export Expiry Analytics CSV\n10. Exit")
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

if _name_ == "_main_":
    main()
