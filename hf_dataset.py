from datasets import load_dataset
from config import DATASET

ds = load_dataset(DATASET)

print(type(ds))
print(ds["train"][:4])
print(type(ds["train"]))