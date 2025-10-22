from fastapi import FastAPI , UploadFile, File
import tempfile
import os
from utils.transcribe import transcribe_audio
from utils.translate import translate_hindi_to_english


app = FastAPI()

@app.get("/")
def root():
    return {"ASR system"}

@app.post("/transcribe/")
async def upload_audio(file: UploadFile = File(...)):

    with tempfile.NamedTemporaryFile(delete=False, suffix=os.path.splitext(file.filename)[1]) as temp_file:
        temp_file.write(await file.read())
        temp_file_path = temp_file.name

    transcription = transcribe_audio(temp_file_path)

    return {"filename": file.filename, "transcription": transcription}

@app.post("/translate/")
async def translate_text(hindi_text: str):
    
    english_text = translate_hindi_to_english(hindi_text)
    return {"hindi_text": hindi_text, "english_text": english_text}