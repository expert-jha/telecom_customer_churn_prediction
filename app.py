import streamlit as st
import pandas 
import joblib

# Load the saved models
rf_model = joblib.load('RandomForest_model.pkl')
lgb_model = joblib.load('LightGBM_model.pkl')


# App title
st.title("Churn Prediction App")

# Sidebar for user input
st.sidebar.header("User Input Features")

# Function to take user input
def user_input_features():
    Subscription_Length = st.sidebar.number_input("Subscription Length (months)", min_value=0, value=12, step=1)
    Charge_Amount = st.sidebar.number_input("Charge Amount", min_value=0.0, value=50.0, step=1.0)
    Seconds_of_Use = st.sidebar.number_input("Seconds of Use", min_value=0.0, value=500.0, step=10.0)
    Frequency_of_use = st.sidebar.number_input("Frequency of Use", min_value=0, value=10, step=1)
    Distinct_Called_Numbers = st.sidebar.number_input("Distinct Called Numbers", min_value=0, value=15, step=1)
    Age = st.sidebar.number_input("Age", min_value=18, value=25, step=1)
    Customer_Value = st.sidebar.number_input("Customer Value", min_value=0.0, value=100.0, step=1.0)

    data = {
        'Subscription Length': Subscription_Length,
        'Charge Amount': Charge_Amount,
        'Seconds of Use': Seconds_of_Use,
        'Frequency of use': Frequency_of_use,
        'Distinct Called Numbers': Distinct_Called_Numbers,
        'Age': Age,
        'Customer Value': Customer_Value
    }

    return pandas.DataFrame(data, index=[0])

# Get user input
input_df = user_input_features()

# Display user input
st.subheader("User Input Features")
st.write(input_df)

# Select model
model_choice = st.selectbox("Choose a model", ["RandomForest", "LightGBM"])

# Predict and display result
if st.button("Predict"):
    if model_choice == "RandomForest":
        model = rf_model
    elif model_choice == "LightGBM":
        model = lgb_model
    

    # Perform prediction
    prediction = model.predict(input_df)[0]
    prediction_prob = model.predict_proba(input_df)[0]

    # Display the prediction
    if prediction == 1:
        st.subheader("Prediction: The customer is likely to churn.")
    else:
        st.subheader("Prediction: The customer is unlikely to churn.")

    # Display prediction probabilities
    st.write(f"Churn Probability: {prediction_prob[1]:.2f}")
    st.write(f"Non-Churn Probability: {prediction_prob[0]:.2f}")
