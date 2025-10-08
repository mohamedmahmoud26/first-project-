import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder, LabelEncoder
from sklearn.compose import ColumnTransformer
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
import joblib


# Load model
def load_model():
    model = joblib.load("../Model/trained_model.pkl")
    preprocessor = joblib.load("../Model/preprocessor.pkl")
    return model, preprocessor


def transform_data(data, preprocessor_path="../Model/preprocessor.pkl"):
    # Load all encoders and preprocessor
    saved = joblib.load(preprocessor_path)
    label_encoders = saved['label_encoders']
    preprocessor = saved['preprocessor']

    # Apply saved label encoders for binary features
    for col, le in label_encoders.items():
        if col in data.columns:
            # handle unseen labels safely
            data[col] = data[col].apply(lambda x: x if x in le.classes_ else le.classes_[0])
            data[col] = le.transform(data[col])

    # Apply same preprocessing as before
    processed_data = preprocessor.transform(data)

    return processed_data


def predict(data):
    model, _ = load_model()
    processed_data = transform_data(data)
    prediction = model.predict(processed_data)
    prediction[:] = min(prediction, 20)
    return np.round(prediction)






