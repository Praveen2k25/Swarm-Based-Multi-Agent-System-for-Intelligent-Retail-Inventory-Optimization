class SupplierAgent:
    def __init__(self, supplier_id):
        self.supplier_id = supplier_id

    def produce_stock(self, product_id, quantity):
        print(f"Supplier {self.supplier_id} producing {quantity} units of Product {product_id}")
        return True
