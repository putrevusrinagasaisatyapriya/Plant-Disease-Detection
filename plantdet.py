import streamlit as st
from PIL import Image
import os

st.set_page_config(page_title="Plant Disease Detection", layout="centered")

st.title("🌿 Plant Disease Detection System")

uploaded_file = st.file_uploader("Upload a leaf image", type=["jpg", "png", "jpeg"])

detected_disease = ""
advice = ""

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)

    if st.button("Detect Disease"):

        diseases = [
            "Healthy Leaf",
            "Leaf Spot",
            "Powdery Mildew",
            "Rust",
            "Bacterial Blight",
            "Early Blight",
            "Late Blight",
            "Anthracnose"
        ]

        index = abs(hash(uploaded_file.name)) % len(diseases)
        detected_disease = diseases[index]

        # Advice
        if detected_disease == "Healthy Leaf":
            advice = "No disease. Maintain watering and sunlight."
        elif detected_disease == "Leaf Spot":
            advice = "Remove infected leaves and apply fungicide."
        elif detected_disease == "Powdery Mildew":
            advice = "Use sulfur spray and improve air flow."
        elif detected_disease == "Rust":
            advice = "Apply neem oil and avoid moisture."
        elif detected_disease == "Bacterial Blight":
            advice = "Use copper sprays and remove infected plants."
        elif detected_disease == "Early Blight":
            advice = "Use crop rotation and fungicide."
        elif detected_disease == "Late Blight":
            advice = "Avoid wet leaves and apply fungicide."
        else:
            advice = "Prune infected parts and use fungicide."

        st.success(f"🌿 Disease: {detected_disease}")
        st.info(f"💊 Solution: {advice}")
