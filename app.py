from flask import Flask, render_template, request, redirect, url_for, session
from agents.store_agent import StoreAgent
from agents.warehouse_agent import WarehouseAgent
from swarm.swarm_routing import swarm_decision
import pandas as pd

app = Flask(__name__)
app.secret_key = 'xyzabc' 

def load_agents():
    demand_df = pd.read_csv("data/demand_forecasting.csv")
    inventory_df = pd.read_csv("data/inventory_monitoring.csv")

    warehouses = []
    stores_dict = {}  

    for idx, row in inventory_df.iterrows():
        warehouse_id = f"W{idx+1}"  
        product_id = str(row['Product ID'])
        stock = row['Stock Levels']
        warehouses.append(WarehouseAgent(warehouse_id, {product_id: stock}))

    for _, row in demand_df.iterrows():
        store_id = str(row['Store ID'])
        product_id = str(row['Product ID'])
        demand = row.get('Demand', row.get('Sales Quantity', 0))

        if store_id not in stores_dict:
            stores_dict[store_id] = {}

        stores_dict[store_id][product_id] = stores_dict[store_id].get(product_id, 0) + demand

    stores = [StoreAgent(store_id, product_map) for store_id, product_map in stores_dict.items()]
    agents = {'stores': stores, 'warehouses': warehouses}

    return agents, demand_df

@app.route('/', methods=['GET', 'POST'])
def index():
    results = []
    product_id = ''

    if request.method == 'POST':
        product_id = request.form['product_id'].strip()
        product_id = str(product_id)

        
        session['product_id'] = product_id
        return redirect(url_for('index'))

    elif request.method == 'GET' and 'product_id' in session:
        product_id = session.pop('product_id')  
        agents, demand_df = load_agents()

        demand_map = {}
        for _, row in demand_df.iterrows():
            store_id = str(row['Store ID'])
            pid = str(row['Product ID'])
            demand = row.get('Demand', row.get('Sales Quantity', 0))

            if store_id not in demand_map:
                demand_map[store_id] = {}
            demand_map[store_id][pid] = demand_map[store_id].get(pid, 0) + demand

        results = swarm_decision(agents, product_id, demand_map)

        
        print("Submitted Product ID:", product_id)
        print("Routing Results:", results)

    return render_template('index.html', results=results, product_id=product_id)

if __name__ == '__main__':
    app.run(debug=True)
