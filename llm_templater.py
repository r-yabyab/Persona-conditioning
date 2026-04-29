import jsonlines

# puts into QA pairs for PEFT

            # conversation = [
            #     {
            #         "role": "user",
            #         "content": item['question']
            #     },
            #     {
            #         "role": "assistant", 
            #         "content": item['answer']
            #     }
            # ]
          
input_data = "./data/pairs_grouped_topics_filtered.jsonl"
output = "./data/qa_pairs.jsonl"
            
ROLE_MAP = {
    "Person_1": "user",
    "Person_2": "assistant",
}

def main():
    with jsonlines.open(input_data, "r") as reader, \
        jsonlines.open(output, "w") as writer:
        for point in reader:
            conversation = [
                {"role": ROLE_MAP.get(msg["role"], msg["role"]), "content": msg["content"]}
                for msg in point["messages"]
            ]
            writer.write({"conversations": conversation})


main()