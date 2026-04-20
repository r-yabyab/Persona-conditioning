import os
import json

root = "./data/messages"

def main():
    for file in os.listdir(root):
        folder_path = os.path.join(root, file)

        if os.path.isdir(folder_path):
            for file in os.listdir(folder_path):
                if file.endswith(".json"):
                    print(file, folder_path)

def count_words():
    with open(r"data\messages\c249294030477852672\messages.json", "r") as reader:
        for line in json.load(reader):
            print(line["Contents"])

def count_json_lines():
    with open(r"data\messages\c249294030477852672\messages.json", "r") as reader:
        print(len(json.load(reader)))

# main()
# count_words()
count_json_lines()