from search import load_index,get_text_embedding,get_index,model,processor
from get_image_data import get_image_path
from fastapi import FastAPI
# from backend. import GalleryDB

app = FastAPI()

@app.get("/search")
def get_images_path(prompt : str):
    query = prompt
    limit = 200

    index = load_index()
    text_embedding = get_text_embedding(query.lower(), model, processor)
    indexes = get_index(text_embedding, index,limit=limit)
    
    image_paths = get_image_path(indexes)

    return {"images":image_paths}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)