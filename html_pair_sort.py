import jsonlines

def main():

    data = []

    # with jsonlines.open("./data/pairs.jsonl", "r", encoding="utf-8") as reader:
    with jsonlines.open("./data/pairs.jsonl", "r") as reader:
        for line in reader:
            data.append(line)
    
    max_score = data[0]

    for i in range(len(data) - 1):
        for j in range(len(data)):
            current = data[i]["cos_sim"]
            next = data[j]["cos_sim"]
            if current > next:
                temp = current
                current = next
                next = temp

    for point in data:
        print(point["cos_sim"])
                


main()