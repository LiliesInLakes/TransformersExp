Going through the pipeline docs

I am on a journey to explore the transformers repo of Hugging Face. So I went through th pipeline docs. 
First of all, the code is written for notebooks. If you run it in a script form, you will need to print the result separately. 
from transformers import pipeline
pipeline = pipeline(task="automatic-speech-recognition", model="openai/whisper-large-v3")
pipeline("https://huggingface.co/datasets/Narsil/asr_dummy/resolve/main/mlk.flac")
 
to script ->from transformers import pipeline
pipeline = pipeline(task="automatic-speech-recognition", model="openai/whisper-large-v3")
mine = pipeline("https://huggingface.co/datasets/Narsil/asr_dummy/resolve/main/mlk.flac")

from transformers import pipeline
pipeline = pipeline(task="text-generation", model="google/gemma-2–2b")
pipeline("the secret to baking a really good cake is ")
[{'generated_text': 'the secret to baking a really good cake is 1. the right ingredients 2. the'}]
access to gemma-2–2b is restricted.


Serve CLI: lightweight server. 
    pip install transformers[serving] ->> this has issue on zsh. zsh cant handle the brackets as is. 
        We need to write pip install 'transformers[serving]' OR pip isntall transformers\[serving\] instead
