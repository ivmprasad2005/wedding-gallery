from fastapi import FastAPI, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
import os

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"message": "Wedding gallery server working!"}

@app.post("/upload")
def upload_photo(file: UploadFile):
    os.makedirs("uploads", exist_ok=True)
    file_path = f"uploads/{file.filename}"
    with open(file_path, "wb") as f:
        f.write(file.file.read())
    return {"message": "Photo uploaded successfully!", "filename": file.filename}

os.makedirs("uploads", exist_ok=True)
app.mount("/photos", StaticFiles(directory="uploads"), name="photos")

@app.get("/list")
def list_photos():
    files = os.listdir("uploads")
    return {"photos": files}

app.mount("/", StaticFiles(directory=".", html=True), name="static")