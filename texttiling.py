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

    data = "\n\n".join(item["message"] for item in data)
    # data = "\n\n".join(f'{item["author"]}: {item["message"]}' for item in data)
    # data = "\n\n".join(data)

    # print(type(data))
    tt = TextTilingTokenizer()
    segments = tt.tokenize(data)

    vectorizer = TfidfVectorizer(stop_words="english")
    tfidf = vectorizer.fit_transform(segments)
    features = vectorizer.get_feature_names_out()

    # def top_words(row, n=4):
    #     scores = tfidf[row].toarray().flatten()
    #     top_idx = scores.argsort()[::-1][:n]
    #     return [features[i] for i in top_idx if scores[i] > 0]

    with jsonlines.open("./data/rawtext_texttiling.jsonl", "w") as writer:
        for i, seg in enumerate(segments):
            writer.write({
                # "topics": top_words(i),
                "segment": seg,
            })
            
        # with jsonlines.open("./data/rawtext_texttiling.jsonl", "w") as writer:
        #     for seg in segments:
        #         print("--------------------------------")
        #         print("--------------------------------")
        #         print(seg)
        #         writer.write(seg)


main()