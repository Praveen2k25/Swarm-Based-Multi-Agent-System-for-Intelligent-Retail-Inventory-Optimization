class WarehouseAgent:
    def __init__(self, warehouse_id, stock_levels):
        self.warehouse_id = warehouse_id
        self.stock_levels = stock_levels

    def supply_stock(self, product_id, quantity):
        if self.stock_levels.get(product_id, 0) >= quantity:
            self.stock_levels[product_id] -= quantity
            return True
        return False
