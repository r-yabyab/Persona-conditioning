"""
Reads files

Todo:
- read line by line
- append if multiple comments per person
"""

import os
import json

root = "./data/localex/msg/dms"

def main():
    print(len(os.listdir(root)))

main()