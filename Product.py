class Product:
    def _init_(self, name, quantity, expiry_date):
        self.name = name
        self.quantity = quantity
        self.expiry_date = datetime.strptime(expiry_date, "%Y-%m-%d").date()
        self.added_time = datetime.now()  

    def days_until_expiry(self):
        today = datetime.today().date()
        return (self.expiry_date - today).days

    def _lt_(self, other):
       
        return self.expiry_date < other.expiry_date

    def _str_(self):
        days = self.days_until_expiry()
        status = "Expired" if days < 0 else f"Near expiry ({days} days)" if days <= 3 else "Valid"
        return f"{self.name} | Qty: {self.quantity} | Expiry: {self.expiry_date} | Status: {status}"
