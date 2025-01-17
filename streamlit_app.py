import streamlit as st
import requests
import json
from PIL import Image
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import io
import base64

# FastAPI endpoint URL
API_URL = "http://127.0.0.1:8000/predict/"

# Paths to the images
background_image_path = "C:/Users/Sabii/OneDrive/Desktop/object detection project/images/background.jpg"
logo_image_path = "C:/Users/Sabii/OneDrive/Desktop/object detection project/images/iub_logo.jpg"

# Function to encode the local image as base64
def get_base64_image(image_path):
    try:
        with open(image_path, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode()
    except FileNotFoundError:
        st.error(f"File not found: {image_path}")
        return None

# Encode images
background_base64 = get_base64_image(background_image_path)
logo_base64 = get_base64_image(logo_image_path)

# Function to draw predictions on the image
def draw_predictions(image, predictions):
    fig, ax = plt.subplots(1, figsize=(10, 10))
    ax.imshow(image)

    for pred in predictions:
        x_center, y_center, width, height = pred.get('box', [0, 0, 0, 0])
        confidence = pred.get('confidence', 0)
        name = pred.get('name', 'Unknown')

        x1 = int(x_center - width / 2)
        y1 = int(y_center - height / 2)
        x2 = int(x_center + width / 2)
        y2 = int(y_center + height / 2)

        rect = patches.Rectangle(
            (x1, y1), x2 - x1, y2 - y1, linewidth=2, edgecolor="red", facecolor="none"
        )
        ax.add_patch(rect)
        ax.text(
            x1,
            y1 - 5,
            f"{name} ({confidence:.2f})",
            color="white",
            fontsize=10,
            bbox=dict(facecolor="red", alpha=0.5),
        )

    plt.axis("off")
    buf = io.BytesIO()
    plt.savefig(buf, format="png", bbox_inches="tight")
    buf.seek(0)
    return buf

# Streamlit App Layout
st.set_page_config(
    page_title="FYP Project",
    page_icon="🤖",
    layout="wide",
)

# Custom CSS to maintain full opacity of the wallpaper
st.markdown(
    f"""
    <style>
    body {{
        background-image: url('data:image/jpeg;base64,{background_base64}');
        background-size: cover;
        background-attachment: fixed;
        background-position: center;
        background-color: transparent; /* Keep wallpaper fully visible */
    }}
    .stApp {{
        background-color: transparent;  /* No background color for content area */
        padding: 10px;
        border-radius: 15px;
    }}
    h1, h2 {{
        color: white;
        text-align: center;
        font-family: 'Trebuchet MS', sans-serif;
        text-shadow: 2px 2px 8px rgba(0, 0, 0, 0.7);
    }}
    h1 {{
        font-size: 3em;
    }}
    h2 {{
        font-size: 1.5em;
        margin-bottom: 20px;
    }}
    .stButton, .stDownloadButton {{
        border-radius: 12px;
        padding: 10px 20px;
        font-size: 16px;
        transition: background-color 0.3s;
    }}
    .stButton {{
        background-color: #4CAF50;
        color: white;
    }}
    .stButton:hover {{
        background-color: #45a049;
    }}
    .stDownloadButton {{
        background-color: #2196F3;
        color: white;
    }}
    .stDownloadButton:hover {{
        background-color: #0b7dda;
    }}
    .prediction-card {{
        background-color: rgba(255, 255, 255, 0.8);
        border-radius: 10px;
        padding: 10px;
        margin: 5px 0;
        box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
    }}
    .prediction-name {{
        font-size: 16px;
        font-weight: bold;
        color: #2980b9;
    }}
    .prediction-confidence {{
        font-size: 14px;
        color: #27ae60;
    }}
    </style>
    <img id="university-logo" src="data:image/jpeg;base64,{logo_base64}" alt="University Logo">
    """,
    unsafe_allow_html=True,
)

# Header Section
st.markdown("""
<h1>OBJECT X 🚀</h1>
<h2>Upload an image and let <span style='color: #FFD700; text-shadow: 1px 1px 5px rgba(255, 215, 0, 0.8);'>YOLO</span> detect objects for you!</h2>
""", unsafe_allow_html=True)
st.markdown("---")

# File Upload Section
uploaded_file = st.file_uploader(
    "📤 Choose an image file (jpg, jpeg, png)",
    type=["jpg", "jpeg", "png"],
    help="Select an image file to analyze",
)

# Reset Button
if st.button("🔄 Reset"):
    st.experimental_rerun()

if uploaded_file is not None:
    # Display the uploaded image
    col1, col2 = st.columns([1, 1])
    with col1:
        st.image(uploaded_file, caption="Uploaded Image", use_container_width=True)

    with st.spinner("🔍 Analyzing the image..."):
        response = requests.post(API_URL, files={"file": uploaded_file.getvalue()})

    if response.status_code == 200:
        result = response.json()
        predictions = result.get("predictions", [])

        if isinstance(predictions, str):
            predictions = json.loads(predictions)

        with col2:
            st.subheader("🔎 Predictions")
            for pred in predictions:
                name = pred['name']
                confidence = pred['confidence']
                st.markdown(
                    f"""
                    <div class="prediction-card">
                        <div class="prediction-name">{name}</div>
                        <div class="prediction-confidence">Confidence: {confidence:.2f}</div>
                    </div>
                    """,
                    unsafe_allow_html=True,
                )

        img_buf = draw_predictions(Image.open(uploaded_file), predictions)

        # Display the output image with a larger size
        st.image(img_buf, caption="Object Detection Result", use_container_width=False, width=800)
        st.download_button(
            label="📥 Download Image with Predictions",
            data=img_buf,
            file_name="detection_result.png",
            mime="image/png",
        )
    else:
        st.error(f"Error: {response.status_code} - {response.text}")

# Footer
st.markdown("---")
st.markdown("<p style='text-align: center; color: white;'>Made by ❤️ Sohaib Nadeem & Zubair Lodhi</p>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-weight: bold; color: white;'>Created by final-year Data Science students at Islamia University, A Real-Time Object Detection App combines innovative research with seamless integration of FastAPI and Streamlit, exploring various subjects within data science and advancing real-time application development.</p>", unsafe_allow_html=True)
