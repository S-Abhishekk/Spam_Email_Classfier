import streamlit as st
import joblib
import pandas as pd

st.set_page_config(page_title="Spam Classifier", layout="centered")
st.title("📧 Spam Email Classifier")

st.markdown("This app loads and classifies data from the **spambase.data** file directly.")

# Load data from file
try:
    df = pd.read_csv("spambase.data", header=None)
    df.columns = [f"feature_{i}" for i in range(57)] + ["label"]
    X = df.drop(columns=["label"])
    y = df["label"]

    # Load model
    model = joblib.load("spam_classifier.pkl")
    preds = model.predict(X)

    result_df = pd.DataFrame({
        "Prediction": preds,
        "Actual": y
    }).replace({0: "Not Spam", 1: "Spam"})

    st.subheader("🔍 Prediction Results")
    st.dataframe(result_df.head(20))

    accuracy = (result_df["Prediction"] == result_df["Actual"]).mean()
    st.metric(label="✅ Accuracy on spambase.data", value=f"{accuracy * 100:.2f}%")

except Exception as e:
    st.error(f"Error loading data or model: {e}")
