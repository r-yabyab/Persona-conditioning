import jsonlines
"""
filters out freshly segmented conversations

TODO:
score each conversation by similarity
filter by char num
"""


input_segments = "./data/pairs_grouped_topics.jsonl"
output = "./data/pairs_grouped_topics_filtered.jsonl"

def main():
    
    data = []
    
    with jsonlines.open(input_segments, "r") as reader, \
    jsonlines.open(output, "w") as writer:
        for i, point in enumerate(reader):
            if i > 1317:
                break
            print(point)
            conversation_turns = len(point["messages"])
            print(conversation_turns)
            if conversation_turns <= 3:
                writer.write(point)
            
main()