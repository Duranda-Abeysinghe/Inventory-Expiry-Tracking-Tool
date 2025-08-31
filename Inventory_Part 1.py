class InventoryExpiryTracker:
    def _init_(self):
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
        return None
