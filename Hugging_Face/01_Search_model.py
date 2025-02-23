# pip install huggingface_hub
# Install this package to query about hugging face programatically. like below one in which we are going to find text-classification model sorted by downloads in desc order. 

from huggingface_hub import HfApi
hugging_api = HfApi()


models = hugging_api.list_models(
    filter=ModelFilter(task="Image-Text-to-Text"),
    sort="downloads",
    direction=-1,
  	limit=1
)

model_list = list(models)

for item in model_list:
  print(item.id)
