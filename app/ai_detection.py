from openai import OpenAI
from app.config import OPENAI_API_KEY
from sklearn.metrics.pairwise import cosine_similarity

client = OpenAI(api_key=OPENAI_API_KEY)

def embed(text):
    return client.embeddings.create(
        model="text-embedding-3-small",
        input=text
    ).data[0].embedding

def detect(answer):
    ref = embed("This is a generic AI response")
    vec = embed(answer)

    sim = cosine_similarity([vec], [ref])[0][0]

    if sim > 0.85:
        return "AI-like"

    if len(answer.split()) > 120:
        return "Suspicious"

    return "Human-like"
