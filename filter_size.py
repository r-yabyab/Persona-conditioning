import json
import jsonlines
from itertools import islice

data = []

def main():
    pass

def filter_size_small():
    with jsonlines.open("./data/data_copy.jsonl", "r") as reader, \
        jsonlines.open("./data/filtered.jsonl", "w") as writer:
        for i, line in enumerate(islice(reader, 1, 201), start=1):
            prompt = line["conversations"][0]["content"]
            print(prompt, f"- (index = {i})")
            print("Word count -", word_count(prompt))
            if word_count(prompt) > 100:
                writer.write(line)


    # with open("filtered.jsonl", "x") as f:
        
        

def word_count(x):
    return len(list(x))
    

filter_size_small()