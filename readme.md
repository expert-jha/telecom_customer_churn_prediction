

# **Churn Prediction Streamlit App**

## **Project Overview**
This project is a machine learning application designed to predict customer churn using a dataset containing features such as call failure, complaints, subscription length, charge amount, and more. The app is built with Python and uses **Streamlit** to provide a user-friendly interface for predictions.

The project involves:
1. Selecting the 7 most important features for the Random Forest model.
2. Hyperparameter tuning for three machine learning models:
   - Random Forest
   - LightGBM
   - XGBoost
3. Creating a pipeline for preprocessing and training.
4. Saving the best-performing models.
5. Building a Streamlit app to predict churn using the Random Forest model.

---

## **Features**
- **Machine Learning Models**:
  - Random Forest
  - LightGBM
  - XGBoost
- **Feature Selection**: Focused on the 7 most important features.
- **Preprocessing Pipeline**:
  - Scaling for numeric features.
  - Ordinal encoding for categorical features.
- **Streamlit App**:
  - User input fields for the selected features.
  - Predicts churn using the Random Forest model.

---

## **Technologies Used**
- **Programming Language**: Python
- **Libraries**:
  - **Machine Learning**: `scikit-learn`, `xgboost`, `lightgbm`
  - **Model Saving**: `joblib`
  - **Web App Development**: `streamlit`
- **Version Control**: GitHub

---

## **Installation**

### Prerequisites
- Python (3.8 or above)
- A virtual environment for dependency management

### Clone the Repository
```bash
git clone https://github.com/your-username/churn-prediction-app.git
cd churn-prediction-app
```

### Set Up a Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate     # On Windows
```

### Install Required Libraries
```bash
pip install -r requirements.txt
```

---

## **How to Run**

1. **Train the Models**:
   Run the `model_training.py` script to train the models and save them.
   ```bash
   python model_training.py
   ```
2. **Start the Streamlit App**:
   Run the `app.py` file to launch the Streamlit app.
   ```bash
   streamlit run app.py
   ```
3. **Access the App**:
   Open the app in your web browser at `http://localhost:8501`.

---

## **Project Files**
- `model_training.py`: Script for preprocessing, hyperparameter tuning, and saving models.
- `app.py`: Streamlit application for predicting churn using the Random Forest model.
- `RandomForest_model.pkl`: Saved Random Forest model.
- `LightGBM_model.pkl`: Saved LightGBM model.
- `XGBoost_model.pkl`: Saved XGBoost model.
- `README.md`: Project documentation.

---

## **Usage**
- Enter the values for the 7 selected features in the Streamlit app.
- Click **Predict** to see the churn prediction.

---

## **Model Performance**
- **Random Forest**: (Add accuracy, precision, recall, etc., after evaluation)
- **LightGBM**: (Add performance metrics)
- **XGBoost**: (Add performance metrics)

---

## **Future Enhancements**
- Add support for other models (LightGBM and XGBoost) in the Streamlit app.
- Include feature importance visualization.
- Enhance hyperparameter tuning for better performance.

---

## **License**
This project is licensed under the MIT License. See the LICENSE file for details.

---

## **Contact**
For any queries or suggestions, feel free to contact:

- **Name**: Govind Jha
- **Email**: expert.govindjha@gmail.com

