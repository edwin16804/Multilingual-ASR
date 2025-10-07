from fastapi import FastAPI , UploadFile, File
import tempfile
import os
from utils.transcribe import transcribe_audio



app = FastAPI()

@app.get("/")
def root():
    return {"ASR system"}

@app.post("/upload-audio/")
async def upload_audio(file: UploadFile = File(...)):

    with tempfile.NamedTemporaryFile(delete=False, suffix=os.path.splitext(file.filename)[1]) as temp_file:
        temp_file.write(await file.read())
        temp_file_path = temp_file.name

    transcription = transcribe_audio(temp_file_path)

    return {"filename": file.filename, "transcription": transcription}