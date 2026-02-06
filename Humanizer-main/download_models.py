import os
from transformers import T5Tokenizer, T5ForConditionalGeneration

models = [
    "t5-small",
    "t5-base", 
    "Vamsi/T5_Paraphrase_Paws",
    "humarin/chatgpt_paraphraser_on_T5_base"
]

models_dir = "models"
if not os.path.exists(models_dir):
    os.makedirs(models_dir)

for model_name in models:
    print(f"Downloading {model_name}...")
    try:
        tokenizer = T5Tokenizer.from_pretrained(model_name, cache_dir=models_dir)
        model = T5ForConditionalGeneration.from_pretrained(model_name, cache_dir=models_dir)
        print(f"✓ {model_name} downloaded successfully")
    except Exception as e:
        print(f"✗ Failed to download {model_name}: {e}")
