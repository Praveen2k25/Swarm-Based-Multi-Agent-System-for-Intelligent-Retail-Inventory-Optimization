from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import LabelEncoder

class DemandPredictor:
    def __init__(self):
        self.model = RandomForestRegressor()
        self.store_encoder = LabelEncoder()
        self.product_encoder = LabelEncoder()

    def train(self, df):
        df = df.copy()
        df = df.dropna()
        df['Store ID'] = self.store_encoder.fit_transform(df['Store ID'])
        df['Product ID'] = self.product_encoder.fit_transform(df['Product ID'])
        X = df[['Store ID', 'Product ID']]
        y = df['Sales Quantity']
        self.model.fit(X, y)

    def predict(self, store_id, product_id):
        try:
            sid = self.store_encoder.transform([store_id])[0]
            pid = self.product_encoder.transform([product_id])[0]
            return self.model.predict([[sid, pid]])[0]
        except ValueError:
            return 0  # Unknown store/product
