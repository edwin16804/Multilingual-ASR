import re
import torch
import librosa
from transformers import Wav2Vec2ForCTC, Wav2Vec2Processor


repo_name = "Ed-168/wav2vec2-large-xls-r-300m-hi"
model = Wav2Vec2ForCTC.from_pretrained(repo_name).to("cuda")
processor = Wav2Vec2Processor.from_pretrained(repo_name)


def transcribe_audio(audio_path):

    speech, sr = librosa.load(audio_path, sr=16000)

    input_values = processor(speech, sampling_rate=16000, return_tensors="pt", padding=True).input_values.to("cuda")


    with torch.no_grad():
        logits = model(input_values).logits


    pred_ids = torch.argmax(logits, dim=-1)
    transcription = processor.batch_decode(pred_ids, skip_special_tokens=True)[0]
    
    return transcription

