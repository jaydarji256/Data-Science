# 🌾 Crop Yield Prediction System

A Machine Learning-based web application that predicts crop yield efficiency using agricultural and environmental factors.

---

## 🚀 Project Overview

This project uses a **Random Forest Regression model** to predict crop efficiency based on key features such as:

* State
* Crop Type
* Crop Year
* Season
* Area
* Production

The model is deployed using a simple and interactive web interface built with Streamlit.

---

## 🧠 Machine Learning Approach

* Algorithm Used: **Random Forest Regressor**
* Initial Model MAE: ~5.74
* Optimized Model MAE: ~2.4
* Feature Selection applied to remove:

  * District (high cardinality, low importance)
  * Production_level (derived feature → data leakage)

This resulted in a **simpler, faster, and more efficient model**.

---

## 📊 Features

* Clean and interactive UI using Streamlit
* Real-time predictions
* Optimized model for performance and size
* Proper feature engineering and selection

---

## 🛠️ Tech Stack

* Python
* scikit-learn
* pandas, numpy
* Streamlit

---

## 📁 Project Structure

```
crop-yield-prediction/
│
├── app.py
├── notebook.ipynb
├── requirements.txt
├── README.md
└── model.pkl  (ignored via .gitignore)
```

---

## ⚠️ Model File Notice

The trained model file (`model.pkl`) is **not included in this repository** due to size limitations.

---

## ▶️ How to Run the Project

### 1. Clone the repository

```
git clone <your-repo-link>
cd crop-yield-prediction
```

### 2. Install dependencies

```
pip install -r requirements.txt
```

### 3. Train the model

Run the notebook to generate the model file:

```
notebook.ipynb
```

This will create:

```
model.pkl
```

---

### 4. Run the Streamlit app

```
python -m streamlit run app.py
```

---

## 💡 Key Learnings

* Importance of feature selection
* Handling data leakage in ML models
* Trade-off between model accuracy and size
* Building end-to-end ML applications
* Deploying ML models with user interfaces

---

## 🚀 Future Improvements

* Add dropdown-based inputs using encoders
* Deploy the app online (Streamlit Cloud / Render)
* Improve UI/UX design
* Add visualization dashboards

---

## 🤝 Contributing

Feel free to fork this repo and improve the project.

---

## 📌 Author

**Jay Darji**

---

## ⭐ If you like this project

Give it a star ⭐ on GitHub!
