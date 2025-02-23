'''Hugging face provide dataset, in this will check few things about dataset
 pip install datasets
 
'''
from datasets import load_dataset_builder

data_builder_obj = load_dataset_builder("taesiri/imagenet_hard_review_data_r2") 
dataset_info = data_builder_obj.info.features
dataset_desc = data_builder_obj.info.description


# Now let's download the dataset
from datasets import load_dataset

review_ds = load_dataset("taesiri/imagenet_hard_review_data_r2", split="train")

print(f"The length of the dataset is {len(review_ds)}")


