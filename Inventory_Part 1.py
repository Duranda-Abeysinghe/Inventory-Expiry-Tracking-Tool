class InventoryExpiryTracker:
    def _init_(self):
        self.expiry_heap = []  # Min Heap for expiry
        self.add_order_list = []  # Keep track of order added
        self.stock_queue = deque()  # FIFO log
        self.threshold = 3  # days for alert
        self.load_inventory()  # Load saved inventory if exists
        self.show_alerts()    # Simple reminder on start

    # Add product
    def add_product(self, product):
        heapq.heappush(self.expiry_heap, product)
        self.add_order_list.append(product)  # track insertion order
        self.stock_queue.append(f"Added: {product.name}")
        self.save_inventory()

    # Remove next expiring product
    def remove_product(self):
        if self.expiry_heap:
            removed = heapq.heappop(self.expiry_heap)
            if removed in self.add_order_list:
                self.add_order_list.remove(removed)
            self.stock_queue.append(f"Removed: {removed.name}")
            self.save_inventory()
            return removed
        return None

    # Update product quantity
    def update_product(self, name, new_qty):
        for prod in self.expiry_heap:
            if prod.name == name:
                prod.quantity = new_qty
                self.stock_queue.append(f"Updated: {prod.name} to {new_qty}")
                heapq.heapify(self.expiry_heap)
                self.save_inventory()
                return prod
        return None
