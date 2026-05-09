from PIL import Image
from transformers import CLIPProcessor, CLIPModel
import torch

# Local model path
MODEL_PATH = "./models/clip-vit-base-patch32"

# Load model
model = CLIPModel.from_pretrained(MODEL_PATH)

# Load processor
processor = CLIPProcessor.from_pretrained(MODEL_PATH)

# Load image
image = Image.open("data/f.jpeg")
# Text prompts
texts = [
    "cat sitting infront of window",
    "dog in red color"
]

# Convert image + text into tensors
inputs = processor(
    text=texts,
    images=image,
    return_tensors="pt",
    padding=True
)

# Disable gradient calculation
with torch.no_grad():
    outputs = model(**inputs)

# Similarity scores
logits_per_image = outputs.logits_per_image

# Convert to probabilities
probs = logits_per_image.softmax(dim=1)

print(probs)