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
sample = "380890688247693314.html"
# message_author = "div.chatlog__message-primary>div>span.chatlog__message-primary"
message_author = "chatlog__message-primary"
    # from message_selector... parent, parent --> message author


def main():
    print(len(os.listdir(root)))
    with open(f"{root}/380890688247693314.html", "r", encoding="utf-8") as reader:
        soup = BeautifulSoup(reader, "html.parser")
        # print(type(soup))
        messages  = soup.select(message_selector)
        # username = messages.find_parentd("div", class="chatlog__message-primary")
        # print(username)
        for message in messages:
            print(message)
            author_tag = message.find_parent("div", class_=message_author).select_one("span", class_="chatlog__author")
            print(author_tag.get_text())
        # print(messages)
        print(type(messages))
        
              


main()