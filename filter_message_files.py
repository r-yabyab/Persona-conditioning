import os
import json

root = "./data/messages"

def main():
    for folder in os.listdir(root):
        folder_path = os.path.join(root, folder)

        if os.path.isdir(folder_path):
            file_path = os.path.join(folder_path, "messages.json")
            print(count_json_lines(file_path), f" {file_path}", sep="")

def count_words():
    with open(r"data\messages\c249294030477852672\messages.json", "r") as reader:
        for line in json.load(reader):
            print(line["Contents"])

def count_json_lines(x):
    # with open(r"data\messages\c249294030477852672\messages.json", "r") as reader:
    #     print(len(json.load(reader)))
    with open(x, "r", encoding="utf-8") as reader:
        return len(json.load(reader))

main()
# count_words()
# count_json_lines()