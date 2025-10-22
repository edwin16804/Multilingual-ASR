from transformers import pipeline
import torch


translator = pipeline(
    "translation",
    model="./fine_tuned_hi_en_BA",
    tokenizer="./fine_tuned_hi_en_BA",
    device=0 if torch.cuda.is_available() else -1 
)

MAX_LEN_EN = 400

def translate_hindi_to_english(hindi_text: str) -> str:
    if not hindi_text or hindi_text.strip() == "":
        return ""

    # Run translation
    translation = translator(hindi_text, max_length=MAX_LEN_EN)
    return translation[0]['translation_text']
