import pandas as pd

def load_inventory(path='data/inventory_monitoring.csv'):
    df = pd.read_csv(path)
    inventory = {}
    for _, row in df.iterrows():
        store_inv = inventory.setdefault(row['Store ID'], {})
        store_inv[row['Product ID']] = row['Stock Levels']
    return inventory
