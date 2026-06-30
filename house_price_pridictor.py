import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

data = {
    'sqft': [800, 1000, 1200, 1500, 1800, 2000, 2200, 2500, 2800, 3000],
    'bedrooms': [2, 2, 3, 3, 3, 4, 4, 4, 5, 5],
    'bathrooms': [1, 1, 2, 2, 2, 3, 3, 3, 4, 4],
    'price': [200000, 220000, 250000, 300000, 320000, 360000, 400000, 450000, 500000, 550000]
}

df = pd.DataFrame(data)

X = df[['sqft', 'bedrooms', 'bathrooms']]
y = df['price']

model = LinearRegression()
model.fit(X, y)

df['predicted_price'] = model.predict(X)

plt.figure(figsize=(10,5))

plt.scatter(df['price'], df['predicted_price'], color='blue', label='Predicted Prices')

plt.plot([df['price'].min(), df['price'].max()],
         [df['price'].min(), df['price'].max()],
         color='red', linestyle='--', label='Perfect Prediction')

plt.xlabel("Actual Price")
plt.ylabel("Predicted Price")
plt.title("Actual vs Predicted House Prices")

plt.legend()
plt.grid(True)
plt.show()
