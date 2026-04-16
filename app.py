import streamlit as st
import pickle
import numpy as np

# -------------------------------
# Load model + encoders
# -------------------------------
@st.cache_resource
def load_assets():
    model = pickle.load(open('finalmodel.pkl', 'rb'))
    encoders = pickle.load(open('encoders.pkl', 'rb'))
    return model, encoders

model, encoders = load_assets()

# -------------------------------
# UI
# -------------------------------
st.set_page_config(page_title="Crop Yield Predictor", layout="centered")

st.title("🌾 Crop Yield Prediction System")

# -------------------------------
# Dropdown Inputs
# -------------------------------
state = st.selectbox("Select State", encoders["State"].classes_)
crop = st.selectbox("Select Crop", encoders["Crop"].classes_)
season = st.selectbox("Select Season", encoders["Season"].classes_)

# -------------------------------
# Numeric Inputs
# -------------------------------
year = st.number_input("Crop Year", min_value=1990, max_value=2035, value=2020)
area = st.number_input("Area", min_value=0.0)
production = st.number_input("Production", min_value=0.0)

# -------------------------------
# Encoding
# -------------------------------
state_enc = encoders["State"].transform([state])[0]
crop_enc = encoders["Crop"].transform([crop])[0]
season_enc = encoders["Season"].transform([season])[0]

# -------------------------------
# Prediction
# -------------------------------
if st.button("Predict"):
    try:
        input_data = np.array([[
            state_enc,
            crop_enc,
            year,
            season_enc,
            area,
            production
        ]])

        prediction = model.predict(input_data)[0]

        st.success(f"🌟 Predicted Crop Efficiency: {round(prediction, 3)}")

    except Exception as e:
        st.error(f"Error: {e}")