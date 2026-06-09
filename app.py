import streamlit as st
import cv2
import pandas as pd
from pathlib import Path

from utils.parser import parse_label_file
from utils.visualization import draw_boxes

st.set_page_config(
    page_title="KITTI Vision Explorer",
    layout="wide"
)

st.title("🚗 KITTI Autonomous Driving Dataset Explorer")

image_dir = Path("data/image_2")
label_dir = Path("data/label_2")

images = sorted(image_dir.glob("*.png"))

if len(images) == 0:
    st.warning("No KITTI images found.")
    st.stop()

selected_image = st.selectbox(
    "Select Image",
    [img.name for img in images]
)

img_path = image_dir / selected_image

label_path = label_dir / selected_image.replace(".png", ".txt")

image = cv2.imread(str(img_path))
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

df = parse_label_file(label_path)

annotated = draw_boxes(image.copy(), df)

col1, col2 = st.columns(2)

with col1:
    st.subheader("Original Image")
    st.image(image)

with col2:
    st.subheader("Bounding Boxes")
    st.image(annotated)

st.subheader("Detected Objects")

st.dataframe(df)

st.subheader("Object Counts")

counts = df["type"].value_counts()

st.bar_chart(counts)
