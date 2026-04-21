"""
Reads files

Todo:
- read line by line
- append if multiple comments per person
"""


import os
import json
from bs4 import BeautifulSoup

root = "./data/localex/msg/dms"
message_selector = "span.chatlog__markdown-preserve" #span
short_timestamp = "chatlog__short-timestamp" #div
sample = "380890688247693314_short.html"
# message_author = "div.chatlog__message-primary>div>span.chatlog__message-primary"
# message_author = "chatlog__message-primary"
message_author = "chatlog__message-group"
    # from message_selector... parent, parent --> message author



def main():
    user_message = ""
    print(len(os.listdir(root)))
    with open(f"{root}/{sample}", "r", encoding="utf-8") as reader:
        soup = BeautifulSoup(reader, "html.parser")
        messages  = soup.select(message_selector)
        # for message in messages:
        for i in range(len(messages) - 1):
            # user_message = ""
            next_message = messages[i+1].find_parent("div", class_=message_author)
            parent = messages[i].find_parent("div", class_=message_author)
            author = parent.select_one("span", class_="chatlog__author").get_text()
            next_author = next_message.select_one("span", class_="chatlog__author").get_text()
            # author = author_tag.get_text()
            timestamp_tag = parent.select_one(".chatlog__timestamp")

            
            # if author == next_message.find_parent("div", class_=message_author).select_one("span", class_="chatlog__author").get_text():
            if author == next_author:
                # print("same")
                user_message += f"{messages[i].get_text()}\n"
            else:
                print("--------")
                user_message += messages[i].get_text()
                print(author)
                print(timestamp_tag["title"])
                print(user_message)
                user_message = ""
            
        print(type(messages))

main()