from transformers import pipeline

pipeline = pipeline(task="automatic-speech-recognition", model="openai/whisper-large-v3")
mine = pipeline("https://huggingface.co/datasets/Narsil/asr_dummy/resolve/main/mlk.flac")
print(mine["text"])
