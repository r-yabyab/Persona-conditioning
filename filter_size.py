import jsonlines
from itertools import islice

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
                writer.write({
                    "prompt": [
                        {"Word count": word_count(prompt), "content": prompt},
                        # {"person": "response", "content": ""}
                    ]
                })
        
        data = []
            
        with jsonlines.open("./data/filtered.jsonl", "r") as content:
            for line in content:
                data.append(line)

        for i in range(len(data)):
            # word_count_first = data[i]["prompt"][0]["Word count"]
            for j in range(i+1, len(data)):
                # word_count_second = data[j]["prompt"][0]["Word count"]
                if (data[i]["prompt"][0]["Word count"] > data[j]["prompt"][0]["Word count"]):
                    temp = data[i]
                    data[i] = data[j]
                    data[j] = temp

        with jsonlines.open("./data/filtered_sort_asc.jsonl", "w") as writer:
            for x in data:
                writer.write(x)

def word_count(x):
    return len(list(x))
    
filter_size_small()