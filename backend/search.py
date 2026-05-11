from PIL import Image
from transformers import CLIPProcessor, CLIPModel
import torch
import torch.nn.functional as F
import os
import numpy as np
import faiss

MODEL_PATH = "./models/clip-vit-base-patch32"

model = CLIPModel.from_pretrained(MODEL_PATH)
processor = CLIPProcessor.from_pretrained(MODEL_PATH)

def load_index():
    return faiss.read_index("db/gallery.index")

def get_text_embedding(text, model, processor):
    text_data = {}
    inputs = processor(text=[text], return_tensors="pt", padding=True)
    features = model.get_text_features(input_ids=inputs['input_ids'],attention_mask=inputs['attention_mask'])
    features = F.normalize(features, p=2, dim=-1)
    text_data['text'] = text
    text_data['text_embeddings'] = features
    return text_data

def get_index(text_embedding, index, limit=30):
    indexes = [int(i) for i in index.search(text_embedding['text_embeddings'].detach().numpy(), limit)[-1][0] if i != -1]  
    return indexes

if __name__ == '__main__':
    query = input("Search : ")

    index = load_index()
    text_embedding = get_text_embedding(query.lower(), model, processor)
    indexes = get_index(text_embedding, index)
    print(indexes)