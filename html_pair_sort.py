import jsonlines
import json

def main():

    data = []

    # with jsonlines.open("./data/pairs.jsonl", "r", encoding="utf-8") as reader:
    with jsonlines.open("./data/pairs.jsonl", "r") as reader:
        for line in reader:
            data.append(line)
    
    max_score = data[0]

    for i in range(len(data) - 1):
        for j in range(i+1, len(data)):
            current = data[i]["cos_sim"]
            next = data[j]["cos_sim"]
            if current < next:
                temp = data[i]
                data[i] = data[j]
                data[j] = temp

    for point in data:
        print(point["cos_sim"])

    with open("./data/pairs_filtered.json", "w") as writer:
        for point in data:
            writer.write(json.dumps({
                "score": point["cos_sim"], 
                "Person1": point["1"]["content"], 
                "Person2": point["2"]["content"]
                }, indent=4))

                


main()