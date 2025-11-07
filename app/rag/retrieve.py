import os, pickle, numpy as np
from sklearn.metrics.pairwise import cosine_similarity
IDX = os.path.join(os.path.dirname(__file__), "index.pkl")

def retrieve_topk(query: str, k: int = 3):
    store = pickle.load(open(IDX, "rb"))
    V, X, D = store["vectorizer"], store["matrix"], store["docs"]
    sims = cosine_similarity(V.transform([query]), X)[0]
    idx = np.argsort(sims)[::-1][:k]
    out = []
    for i in idx:
        d = D[i].copy(); d["score"] = float(sims[i]); out.append(d)
    return out
