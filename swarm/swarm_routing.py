def swarm_decision(agents, product_id, demand_map):
    decisions = []
    for store in agents['stores']:
        needed = demand_map.get(store.store_id, {}).get(product_id, 0)
        if needed > 0:
            for warehouse in agents['warehouses']:
                if warehouse.supply_stock(product_id, needed):
                    decisions.append((warehouse.warehouse_id, store.store_id, product_id, needed))
                    break
    return decisions
