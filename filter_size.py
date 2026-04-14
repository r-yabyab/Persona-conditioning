import json
import jsonlines

data = []

def main():
    pass

def filter_size_small():
    # print("hi")
    # with open("./data/data.jsonl", encoding="utf-8") as f:
    #     # content = f.read()
    #     data.append(f.read())
    #     print(data)
    with jsonlines.open("./data/data_copy.jsonl", "r") as f:
        for i, obj in enumerate(f):
            print(obj, i)
    

filter_size_small()
