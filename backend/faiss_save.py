from PIL import Image
from transformers import CLIPProcessor, CLIPModel
import torch
import torch.nn.functional as F
import os
import numpy as np
import faiss

index = faiss.IndexFlatL2(512)

MODEL_PATH = "./models/clip-vit-base-patch32"
IMAGE_FOLDER = "./data/"

model = CLIPModel.from_pretrained(MODEL_PATH)
processor = CLIPProcessor.from_pretrained(MODEL_PATH)

def get_image_embeddings(image_path,model,processor):
    image_data = {}
    image = Image.open(image_path)
    inputs = processor(images=image, return_tensors="pt", padding=True)
    with torch.no_grad():
        features = model.get_image_features(pixel_values=inputs['pixel_values'])
    features = F.normalize(features, p=2, dim=-1)

    index.add(features.numpy())

    return image_path

def get_image_embeddings_from_folder(folder_path, model, processor):
    for filename in os.listdir(folder_path):
        if filename.endswith(('.png', '.jpg', '.jpeg')):
            image_path = os.path.join(folder_path, filename)
            image_data = get_image_embeddings(image_path, model, processor)
            print(f"{image_data} Added to index")

def save_index(index, filename):
    faiss.write_index(index, filename)

def add_single_image(image_path, index):
    image_data = get_image_embeddings(image_path, model, processor)
    index.add(image_data['image_embeddings'].detach().numpy())
    save_index(index, "db/gallery.index")

if __name__ == '__main__':
    get_image_embeddings_from_folder(IMAGE_FOLDER, model, processor)
    save_index(index, "db/gallery.index")
    print("Save SuccessFull")