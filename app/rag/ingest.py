import os, glob, pickle
from sklearn.feature_extraction.text import TfidfVectorizer

DOC_DIR = os.path.join(os.path.dirname(__file__), "..", "..", "governance")
OUT = os.path.join(os.path.dirname(__file__), "index.pkl")

def main():
    docs = []
    for fp in glob.glob(os.path.join(DOC_DIR, "*.md")):
        text = open(fp, encoding="utf-8").read()
        for i in range(0, len(text), 600):
            docs.append({"id": os.path.basename(fp)+"::"+str(i), "text": text[i:i+600], "source": os.path.basename(fp)})
    vec = TfidfVectorizer(stop_words="english")
    X = vec.fit_transform([d["text"] for d in docs])
    with open(OUT, "wb") as f:
        pickle.dump({"vectorizer": vec, "matrix": X, "docs": docs}, f)
    print(f"Indexed {len(docs)} chunks -> {OUT}")

if __name__ == "__main__":
    main()
