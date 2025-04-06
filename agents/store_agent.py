class StoreAgent:
    def __init__(self, store_id, inventory):
        self.store_id = store_id
        self.inventory = inventory

    def request_stock(self, product_id, needed_qty):
        return {"store_id": self.store_id, "product_id": product_id, "quantity": needed_qty}
