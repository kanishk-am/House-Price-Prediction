# House Price Prediction using Multiple Linear Regression

##  Project Overview

This project demonstrates how to build a **Multiple Linear Regression** model using **Python** and **Scikit-learn** to predict house prices based on three features:

- Square Footage (`sqft`)
- Number of Bedrooms (`bedrooms`)
- Number of Bathrooms (`bathrooms`)

The project also visualizes the model's performance by comparing **Actual Prices** with **Predicted Prices** using a scatter plot.

---

##  Project Structure

```
House-Price-Prediction/
│
├── house_price_prediction.py
├── README.md
└── requirements.txt
```

---

##  Features

- Load and create a housing dataset using Pandas.
- Train a Multiple Linear Regression model.
- Predict house prices.
- Visualize Actual vs Predicted prices.
- Easy-to-understand implementation for beginners.

---

## 🛠️ Technologies Used

- Python 3
- Pandas
- Matplotlib
- Scikit-learn

---

## Dataset

The dataset is manually created within the script and contains the following columns:

| Feature | Description |
|---------|-------------|
| sqft | House size in square feet |
| bedrooms | Number of bedrooms |
| bathrooms | Number of bathrooms |
| price | Actual house price |

Example:

| sqft | bedrooms | bathrooms | price |
|------|----------|------------|--------|
| 800 | 2 | 1 | 200000 |
| 1500 | 3 | 2 | 300000 |
| 3000 | 5 | 4 | 550000 |

---

##  Installation

Clone the repository:

```bash
git clone https://github.com/your-username/House-Price-Prediction.git
```

Navigate to the project folder:

```bash
cd House-Price-Prediction
```

Install the required packages:

```bash
pip install pandas matplotlib scikit-learn
```

Or install using:

```bash
pip install -r requirements.txt
```

---

##  Running the Project

Run the Python script:

```bash
python house_price_prediction.py
```

The program will:

1. Train the Linear Regression model.
2. Predict house prices.
3. Display an Actual vs Predicted scatter plot.

---

##  Output

The output graph contains:

- **Blue dots** representing predicted house prices.
- **Red dashed line** representing perfect predictions.
- A comparison between actual and predicted prices.

---

##  Machine Learning Model

This project uses **Multiple Linear Regression** from Scikit-learn.

Input Features:

- Square Footage
- Bedrooms
- Bathrooms

Target Variable:

- House Price

---

##  Dependencies

```
pandas
matplotlib
scikit-learn
```

---

##  Future Improvements

- Train using a larger real-world housing dataset.
- Split data into training and testing sets.
- Evaluate using metrics such as:
  - R² Score
  - Mean Squared Error (MSE)
  - Mean Absolute Error (MAE)
- Add model serialization using Pickle or Joblib.
- Build a web interface using Flask or Streamlit.

---

##  Author

**Your Name**

**KANISHK A M**
GitHub: https://github.com/kanishk-am

---
