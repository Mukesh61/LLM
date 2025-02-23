'''
saving model locally, can help us to refer it back from local.
'''

from transformers import AutoModel

model_id = "microsoft/OmniParser-v2.0"

pre_model = AutoModel.from_pretrained(modelId)

pre_model.save_pretrained(save_directory=f"models_local/{model_id}")
