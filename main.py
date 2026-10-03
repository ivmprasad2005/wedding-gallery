from fastapi import FastAPI, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
import cloudinary
import cloudinary.uploader
import cloudinary.api
import os

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

cloudinary.config(
    cloud_name="xyvt9vbp",
    api_key="139194367633643",
    api_secret="x7hur4-rxMNzH3S448oKQ5275mI"
)

@app.get("/")
def home():
    return {"message": "Teja Digitals server working!"}

@app.post("/upload/{event}")
def upload_photo(event: str, file: UploadFile):
    result = cloudinary.uploader.upload(
        file.file,
        folder=f"teja-digitals/{event}",
        public_id=file.filename.rsplit(".", 1)[0],
        overwrite=True
    )
    return {"message": "Photo uploaded successfully!", "url": result["secure_url"]}

@app.get("/list/{event}")
def list_photos(event: str):
    result = cloudinary.api.resources(
        type="upload",
        prefix=f"teja-digitals/{event}/",
        max_results=500
    )
    photos = [
        {"filename": r["public_id"].split("/")[-1], "url": r["secure_url"]}
        for r in result.get("resources", [])
    ]
    return {"photos": photos}

@app.get("/events")
def list_events():
    result = cloudinary.api.root_folders()
    teja_folders = cloudinary.api.subfolders("teja-digitals") if any(
        f["name"] == "teja-digitals" for f in result.get("folders", [])
    ) else {"folders": []}
    events = [f["name"] for f in teja_folders.get("folders", [])]
    return {"events": events}

@app.delete("/delete/{event}/{filename}")
def delete_photo(event: str, filename: str):
    public_id = f"teja-digitals/{event}/{filename}"
    cloudinary.uploader.destroy(public_id)
    return {"message": "Photo deleted successfully!"}

@app.delete("/delete-event/{event}")
def delete_event(event: str):
    cloudinary.api.delete_resources_by_prefix(f"teja-digitals/{event}/")
    cloudinary.api.delete_folder(f"teja-digitals/{event}")
    return {"message": "Event deleted successfully!"}

app.mount("/", StaticFiles(directory=".", html=True), name="static")