# Multilingual-ASR

## Datasets

- **Common Voice dataset**
    - Multi-language, open-source voice dataset for training speech-enabled applications.
    - Provides audio chunks and corresponding actual text transcriptions.
    - Example code to load Hindi data:
      ```python
      common_voice_train = load_dataset(
          "mozilla-foundation/common_voice_16_0",
          "hi",
          split="train+validation",
          trust_remote_code=True
      )
      ```

## Models

- **Wav2Vec2-BERT**
    - 580M-parameter versatile audio model, pre-trained on 4.5M hours of unlabeled audio data covering more than 143 languages.
    - Predictions are done in a single pass, making it much faster than sequence-to-sequence models like Whisper.
    - Achieves strong results even with small amounts of training data, adapts easily to any alphabet, and is resource-efficient.
    - Expects input audio as a 1D array sampled at 16 kHz.

- **Wav2Vec2 XLS-R**
    - XLS-R is Facebook AI's cross-lingual large-scale version of Wav2Vec2, trained on more than 436k hours of speech from 128 languages, allowing robust performance on multilingual ASR tasks.
    - XLS-R models (300M, 1B parameters) excel for low-resource languages and offer improved accuracy and generalization compared to standard Wav2Vec2.
    - The architecture includes a feature encoder, transformer layers, and quantization modules, refined for cross-lingual robustness and high performance with limited labeled data.
    - XLS-R 300M is ideal for Hindi and other Indian languages due to its multilingual pretraining and demonstrated effectiveness in ASR settings.

## My Training

- Used the **Wav2Vec2 Large XLS-R 300M** architecture for fine-tuning Hindi ASR.
- **Audio Format:** Mono, 16 kHz WAV files.
- **Dataset:** Mozilla Common Voice Hindi (train + validation splits).
- **Hyperparameters:**
    - Batch Size: 4
    - Gradient Accumulation: 8
    - Learning Rate: 3e-5 (Adam optimizer)
    - Warmup Ratio: 0.1
    - Epochs: 30
    - Mixed Precision (FP16): Enabled (auto-switch with CUDA)
    - Evaluation: Every 500 steps
- **Performance:** Achieved competitive Word Error Rate (WER) compared to baselines; model adapts well to Hindi alphabets.
- The training procedure was resource-efficient and achieved fast convergence thanks to the XLS-R’s robust pretrained representations.

## Key Advantages

- **Multilingual support:** XLS-R can be adapted to any alphabet or language present in Common Voice.
- **Speed and efficiency:** Faster and more data-efficient than sequence-to-sequence ASR models.
- **Superior results for Hindi:** Outperformed Whisper and other baselines on Hindi Common Voice.

***



