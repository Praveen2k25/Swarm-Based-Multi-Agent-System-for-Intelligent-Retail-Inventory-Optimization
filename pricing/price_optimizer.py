import pandas as pd

def optimize_prices(path='data/pricing_optimization.csv'):
    df = pd.read_csv(path)
    df['Optimized Price'] = df['Price'] - (df['Discounts'] * 0.5)
    return df[['Product ID', 'Store ID', 'Optimized Price']]
