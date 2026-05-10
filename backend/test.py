from PIL import Image
from transformers import CLIPProcessor, CLIPModel
import torch
import torch.nn.functional as F
import os

MODEL_PATH = "./models/clip-vit-base-patch32"
IMAGE_FOLDER = "./test_data/"

model = CLIPModel.from_pretrained(MODEL_PATH)
processor = CLIPProcessor.from_pretrained(MODEL_PATH)

def get_image_embeddings(image_path,model,processor):
    image_data = {}
    image = Image.open(image_path)
    inputs = processor(images=image, return_tensors="pt", padding=True)
    with torch.no_grad():
        features = model.get_image_features(pixel_values=inputs['pixel_values'])
    features = F.normalize(features, p=2, dim=-1)

    image_data['image_path'] = image_path
    image_data['image_embeddings'] = features

    return image_data

def get_image_embeddings_from_folder(folder_path, model, processor):
    image_data_list = []
    for filename in os.listdir(folder_path):
        if filename.endswith(('.png', '.jpg', '.jpeg')):
            image_path = os.path.join(folder_path, filename)
            image_data = get_image_embeddings(image_path, model, processor)
            image_data_list.append(image_data)
    return image_data_list

def get_text_embedding(text, model, processor):
    text_data = {}
    inputs = processor(text=[text], return_tensors="pt", padding=True)
    features = model.get_text_features(input_ids=inputs['input_ids'],attention_mask=inputs['attention_mask'])
    features = F.normalize(features, p=2, dim=-1)
    text_data['text'] = text
    text_data['text_embeddings'] = features
    return text_data


image_embeddings = get_image_embeddings_from_folder(IMAGE_FOLDER, model, processor)
query = input("Search : ")
text_embedding = get_text_embedding(query.lower(), model, processor)

# Calculate similarity between text and all images
def calculate_similarity(text_embedding, image_embeddings):
    print(text_embedding['text_embeddings'].shape," ",image_embeddings[0]['image_embeddings'].shape)
    similarities = []
    for image_embedding in image_embeddings:
        similarity = torch.matmul(text_embedding['text_embeddings'], image_embedding['image_embeddings'].T)
        similarities.append({
            'image_path': image_embedding['image_path'],
            'similarity': similarity.item()
        })
    return similarities

similarities = calculate_similarity(text_embedding, image_embeddings)

# Sort by similarity
similarities.sort(key=lambda x: x['similarity'], reverse=True)

print(similarities)
