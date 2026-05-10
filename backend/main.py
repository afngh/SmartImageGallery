from PIL import Image
from transformers import CLIPProcessor, CLIPModel
import torch
import torch.nn.functional as F
import os

MODEL_PATH = "./models/clip-vit-base-patch32"
# IMAGE_FOLDER = "./data/"

model = CLIPModel.from_pretrained(MODEL_PATH)

processor = CLIPProcessor.from_pretrained(MODEL_PATH)

filename = "data/c.jpg"

image = Image.open(filename)

inputs = processor(images=image, return_tensors="pt", padding=True)

# print(inputs)

# features = model.get_image_features(pixel_values=inputs['pixel_values'],return_tensors="pt")

# print(features)


with torch.no_grad():
    features = model.get_image_features(pixel_values=inputs['pixel_values'])

features = F.normalize(features.last_hidden_state, p=2, dim=-1)

print(features)