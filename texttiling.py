import nltk
from nltk import texttiling
from nltk.tokenize import TextTilingTokenizer
import jsonlines
from sklearn.feature_extraction.text import TfidfVectorizer

nltk.download('stopwords')

rawtext = "./data/rawtext.jsonl"

def main():
    # nltk.tokenize.texttiling.TextTilingTokenizer()

    data = []
    with jsonlines.open(rawtext, "r") as reader:
        for line in reader:
            data.append(line)

    # for point in data:
    #     print(point)
        # print(type(point))
    data = "\n\n".join(data)

    # print(type(data))
    tt = TextTilingTokenizer()
    segments = tt.tokenize(data)

    with jsonlines.open("./data/rawtext_texttiling.jsonl", "w") as writer:
        for seg in segments:
            print("--------------------------------")
            print("--------------------------------")
            print(seg)
            writer.write(seg)


main()