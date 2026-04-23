"""
Reads files

Todo:
- read line by line
- append if multiple comments per person
"""


import os
import json
from bs4 import BeautifulSoup
from datetime import datetime
from sentence_transformers import SentenceTransformer
from sentence_transformers.util import cos_sim
import jsonlines

root = "./data/localex/msg/dms"
message_selector = "span.chatlog__markdown-preserve" #span
short_timestamp = "chatlog__short-timestamp" #div
sample = "380890688247693314_short.html"
# message_author = "div.chatlog__message-primary>div>span.chatlog__message-primary"
# message_author = "chatlog__message-primary"
message_author = "chatlog__message-group"
    # from message_selector... parent, parent --> message author



def main():

    # yes, no, hi (maybe keep hi)
    MIN_FIRST_MESSAGE_LEN = 3

    model = SentenceTransformer("all-MiniLM-L6-v2")

    user_message = ""
    print(len(os.listdir(root)))
    with open(f"{root}/{sample}", "r", encoding="utf-8") as reader, \
        open("./data/pairs.jsonl", "w", encoding="utf-8") as writer:
        soup = BeautifulSoup(reader, "html.parser")
        messages  = soup.select(message_selector)
        # for message in messages:
        # for i in range(len(messages) - 1):
        conversation_length = len(messages)
        start = 0
        # end = 25
        end = conversation_length -1

        # get starting person not me
        # cosine_sim with other person
        person_one = { "name": None, "content": ""}
        person_two = { "name": "net", "content": ""}
        counter = 0

        for i in range(start, end):
            # user_message = ""
            next_message = messages[i+1].find_parent("div", class_=message_author)
            parent = messages[i].find_parent("div", class_=message_author)
            author = parent.select_one("span", class_="chatlog__author").get_text()
            next_author = next_message.select_one("span", class_="chatlog__author").get_text()
            # author = author_tag.get_text()
            timestamp = parent.select_one(".chatlog__timestamp")["title"]
            dt = datetime.strptime(timestamp, "%A, %B %d, %Y %H:%M")

            if author != "net":
                person_one["name"] = author

            
            if author == next_author:
                user_message += f"{messages[i].get_text()}\n"
                # person_one["content"] += f"{messages[i].get_text()}\n"
            if author != next_author or i == end - 1 :
                if author == "net":
                    user_message += messages[i].get_text()
                    person_two["content"] = user_message
                    print(person_one)
                    print(person_two)

                    encode_person_one = model.encode(person_one["content"])
                    encode_person_two = model.encode(person_two["content"])
                    score = cos_sim(encode_person_one, encode_person_two)
                    print(score)
                    writer.write(json.dumps(
                        {"1": person_one, 
                         "2": person_two, 
                         "cos_sim": float(score[0][0])}
                    ) + "\n")

                    # clear
                    person_one["content"] = ""
                    person_two["content"] = ""
                    user_message = ""

                else:
                    print("--------")
                    user_message += messages[i].get_text()
                    person_one["content"] = user_message
                    # print(author)
                    # print(timestamp)
                    # print(dt)
                    # print(user_message)
                    # print(person_one)
                    # print(person_two)
                    #person_one.clear()
                    user_message = ""

def raw_text():
    with open(f"{root}/{sample}", "r", encoding="utf-8") as reader, \
    jsonlines.open("./data/rawtext.jsonl", "w") as writer:
        soup = BeautifulSoup(reader, "html.parser")
        messages  = soup.select(message_selector)
        conversation_length = len(messages)
        start = 0
        end = conversation_length -1

        for i in range(start, end):
            parent = messages[i].find_parent("div", class_=message_author)
            author = parent.select_one("span", class_="chatlog__author").get_text()
            writer.write(messages[i].get_text())
            print(messages[i].get_text())
        
# main()
raw_text()