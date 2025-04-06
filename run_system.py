from agents.store_agent import StoreAgent
from agents.warehouse_agent import WarehouseAgent
from agents.supplier_agent import SupplierAgent
from models.demand_predictor import predict_demand
from pricing.price_optimizer import optimize_prices
from utils.helpers import load_inventory
from swarm.swarm_routing import swarm_decision

def run_system():
    demand_map = predict_demand()
    inventory_data = load_inventory()
    price_data = optimize_prices()

    stores = [StoreAgent(sid, inventory_data[sid]) for sid in inventory_data]
    # Initialize warehouse with all products from all stores
    all_product_ids = set(pid for store_data in demand_map.values() for pid in store_data)
    warehouses = [WarehouseAgent('WH1', {pid: 100 for pid in all_product_ids})]


    agents = {
        'stores': stores,
        'warehouses': warehouses,
        'suppliers': [SupplierAgent('S1')]
    }

    for product_id in set(pid for store in demand_map.values() for pid in store):
        decisions = swarm_decision(agents, product_id, demand_map)
        print(f"Routing decisions for Product {product_id}: {decisions}")
