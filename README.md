# Multilingual-ASR
## Datasets
- BhasaAnuvaad
    - AST dataset for indic languages - 13 indian languages
    - audio file , actual text , predicted text , alignment score , en_text 
    - size : 4.68 GB , 247736 rows
    - <pre>dataset_stream = load_dataset("ai4bharat/Spoken-Tutorial", "indic2en", split="hindi", streaming=True)</pre>
- Common voice dataset

    -  multi-language, open-source voice dataset for training speech-enabled applications.
    - audio chunks , actual text
    - <pre>common_voice_train = load_dataset("mozilla-foundation/common_voice_11_0","hi",split="train+validation",trust_remote_code=True)</pre>

## Models

- Wav2Vec2 - BERT
    - It is a 580M-parameters versatile audio model that has been pre-trained on 4.5M hours of unlabeled audio data covering more than 143 languages.
    - Whisper gives a 100% WER (Word Error Rate) for resource poor languages like Malayalam , and it is comaparitively slow as its a sequence - sequence model
    - Wav2Vec2-BERT predicts ASR in a single pass, making it much faster than Whisper.
    - It requires little data to achieve competitive performance, is easily adaptable to any alphabet, and is more resource-efficient.