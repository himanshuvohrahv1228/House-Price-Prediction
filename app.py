import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression

st.title("🏠 House Price Predictor")

# Sample dataset
data = {
    'area': [500, 700, 900, 1100, 1500, 1800, 2000],
    'bedrooms': [1, 2, 2, 3, 3, 4, 4],
    'price': [10, 15, 20, 25, 35, 40, 45]  # in lakhs
}

df = pd.DataFrame(data)

# Model training
X = df[['area', 'bedrooms']]
y = df['price']

model = LinearRegression()
model.fit(X, y)

# Userinput
st.subheader("Enter House Details")

area = st.slider("Area (sq ft)", 500, 2500, 1000)
bedrooms = st.slider("Bedrooms", 1, 5, 2)

# Prediction
if st.button("Predict Price"):
    prediction = model.predict([[area, bedrooms]])
    st.success(f"Estimated Price: ₹ {round(prediction[0], 2)} Lakhs")