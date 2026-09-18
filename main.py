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
    return {"message": "Teja Digitals server working!"}

@app.post("/upload/{event}")
def upload_photo(event: str, file: UploadFile):
    folder = f"uploads/{event}"
    os.makedirs(folder, exist_ok=True)
    file_path = f"{folder}/{file.filename}"
    with open(file_path, "wb") as f:
        f.write(file.file.read())
    return {"message": "Photo uploaded successfully!", "filename": file.filename}

@app.get("/list/{event}")
def list_photos(event: str):
    folder = f"uploads/{event}"
    os.makedirs(folder, exist_ok=True)
    files = os.listdir(folder)
    return {"photos": files}

@app.delete("/delete/{event}/{filename}")
def delete_photo(event: str, filename: str):
    file_path = f"uploads/{event}/{filename}"
    if os.path.exists(file_path):
        os.remove(file_path)
        return {"message": "Photo deleted successfully!"}
    return {"message": "Photo not found!"}

os.makedirs("uploads", exist_ok=True)
app.mount("/photos", StaticFiles(directory="uploads"), name="photos")
app.mount("/", StaticFiles(directory=".", html=True), name="static")