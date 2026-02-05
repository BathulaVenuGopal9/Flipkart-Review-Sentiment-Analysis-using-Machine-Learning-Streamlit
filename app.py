import streamlit as st
import pickle
import re

st.set_page_config(page_title="Flipkart Review Sentiment Analysis", layout="centered")

st.title("🛍️ Flipkart Review Sentiment Analysis")
st.subheader("Predict whether a customer review is Positive or Negative")

# -------- CLEAN FUNCTION (MUST MATCH TRAINING) --------
def Clean(texts):
    cleaned_texts = []
    for text in texts:
        text = str(text).lower()
        text = re.sub(r"http\S+|www\S+", "", text)
        text = re.sub(r"[^a-zA-Z ]", "", text)
        text = text.strip()
        cleaned_texts.append(text)
    return cleaned_texts
# -----------------------------------------------------

@st.cache_resource
def load_model():
    with open("flipkart.pkl", "rb") as f:
        model = pickle.load(f)
    return model

model = load_model()

review = st.text_area("Enter Flipkart Product Review", height=150)

if st.button("Predict Sentiment"):
    if review.strip() == "":
        st.warning("⚠️ Please enter a review text.")
    else:
        try:
            prediction = model.predict([review])[0]

            try:
                prob = model.predict_proba([review])[0]
                confidence = round(max(prob) * 100, 2)
            except:
                confidence = None

            if prediction == 1:
                st.success("✅ Positive Review")
                if confidence:
                    st.info(f"Confidence: {confidence}%")
            else:
                st.error("❌ Negative Review")
                if confidence:
                    st.info(f"Confidence: {confidence}%")

        except Exception as e:
            st.error(f"Prediction Error: {e}")

st.markdown("---")
st.caption("Built using Machine Learning & Streamlit 🚀")

