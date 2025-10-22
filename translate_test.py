from transformers import pipeline



# Load your fine-tuned model
translator = pipeline(
    "translation",
    model="./fine_tuned_hi_en_BA",
    tokenizer="./fine_tuned_hi_en_BA"
)

MAX_LEN_HI = 400
MAX_LEN_EN = 400
# Translate any Hindi sentence
while True:
    hindi_text = input("Enter a Hindi sentence (or 'quit' to exit): ").strip()
    if hindi_text.lower() == "quit":
        break
    translation = translator(hindi_text, max_length=MAX_LEN_EN)
    print(f"🪶 English Translation: {translation[0]['translation_text']}\n")
