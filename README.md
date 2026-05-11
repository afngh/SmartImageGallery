# Smart Semantic Image Gallery

An AI-powered image gallery that lets you search images using natural language — no filenames, no tags required.

> **Example:** Query `"person sitting near green wall"` returns semantically relevant images even if their filenames contain no related words.

---

## How it works

```
Image                          Text Query
  ↓                                ↓
CLIP Image Encoder           CLIP Text Encoder
  ↓                                ↓
Image Embedding              Text Embedding
  ↓                                ↓
FAISS Vector Database   →   FAISS Similarity Search
                                   ↓
                          Top Matching Image IDs
                                   ↓
                          SQLite Metadata Lookup
                                   ↓
                           Image Paths Returned
```

1. **Image embedding** — Each image is processed by the CLIP image encoder into a 512-dimensional vector, normalized and stored in FAISS.
2. **Vector storage** — FAISS holds the embeddings for fast similarity search. SQLite stores image IDs, paths, and metadata separately.
3. **Semantic search** — A user's text prompt is encoded into a text embedding. FAISS compares it against all image embeddings and returns the closest matches.

---

## Tech stack

| Technology | Purpose |
|---|---|
| Python | Core backend |
| FastAPI | API framework |
| PyTorch | Deep learning runtime |
| Transformers | CLIP model |
| FAISS | Vector similarity search |
| SQLite | Metadata storage |
| Pillow | Image processing |

---

## Features

- Natural language image search
- CLIP-based multimodal embeddings (image + text)
- Fast vector retrieval with FAISS
- Persistent FAISS index (no re-embedding on restart)
- SQLite metadata storage
- Auto-generated Swagger API docs
- Extensible backend architecture

---

## Project structure

```
backend/
│
├── apis/
│   ├── __init__.py
│   └── main.py
│
├── data/
│   └── images/
│
├── models/
│   └── clip-vit-base-patch32/
│
├── database/
│   ├── gallery.db
│   └── gallery.index
│
├── search.py
├── get_image_data.py
├── requirements.txt
└── __init__.py
```

---

## Installation

**1. Clone the repository**

```bash
git clone <your-repo-url>
cd smart_gallery
```

**2. Create and activate a virtual environment**

```bash
python -m venv venv

# Linux / macOS
source venv/bin/activate

# Windows
venv\Scripts\activate
```

**3. Install dependencies**

```bash
pip install -r requirements.txt
```

---

## Running the backend

```bash
cd backend
uvicorn apis.main:app --reload
```

---

## API reference

FastAPI auto-generates interactive docs at:

```
http://127.0.0.1:8000/docs
```

### `GET /search`

Returns image paths semantically matching the given prompt.

**Query parameter:** `prompt` (string)

**Example request:**

```
GET /search?prompt=cat sitting on chair
```

**Example response:**

```json
{
  "images": [
    "data/cat1.jpg",
    "data/cat2.jpg"
  ]
}
```

---

## FAISS persistence

The FAISS index is saved to `gallery.index` on disk. On subsequent runs, embeddings are loaded from the file rather than recomputed — only newly added images require embedding generation.

---

## Example use cases

- Smart personal photo gallery
- AI-powered media management system
- Semantic image retrieval for content teams
- Personal image search assistant
- Automated content organization

---

## Future improvements

- [ ] Image upload API
- [ ] Real-time indexing for new uploads
- [ ] Frontend gallery UI
- [ ] User authentication
- [ ] Hybrid search (semantic + metadata filters)
- [ ] Automatic caption generation
- [ ] Distributed vector database support
- [ ] Cloud deployment (AWS / GCP / Azure)
- [ ] Batch embedding pipeline

---

## Learning outcomes

This project demonstrates:

- Multimodal AI systems (vision + language)
- Vector databases and embedding generation
- Semantic search and similarity retrieval
- FastAPI backend architecture
- AI-powered retrieval pipelines

---

## Author

Built by **Afnan** — AI-powered semantic image retrieval using CLIP + FAISS + FastAPI.
