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
    transformers serve
    ok the docs are a bit confusing. jUst running htese two commands doesnt create a chat interface.
    It just creates an api server. 
    /v1/chat/completions only accepts POST requests. 
    transformers chat Qwen/Qwen2.5-0.5B-Instruct 
    this loaded the chat interface to test out the model! super cool. I ran this after turning the transformers server on. This was on a new terminal. When i went back to the server terminal, the /v1/chat/completions HTTP/1.1 was there. it showed the model receiving the request (Qwen) and showed the files being loaded (progress bar)