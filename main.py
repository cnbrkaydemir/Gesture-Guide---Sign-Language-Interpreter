from ultralytics import solutions
import streamlit as st
import os

path = os.path.dirname(os.path.abspath(__file__))
# Load YOLO model
model = os.path.join(path, 'model/sign.pt')  # Replace with your model's path if needed

solutions.inference(model=model)