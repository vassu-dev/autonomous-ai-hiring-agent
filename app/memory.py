from openai import OpenAI
from app.config import OPENAI_API_KEY
from app.database import supabase

client = OpenAI(api_key=OPENAI_API_KEY)

def store(candidate_id, text):
    emb = client.embeddings.create(
        model="text-embedding-3-small",
        input=text
    ).data[0].embedding

    supabase.table("memory").insert({
        "candidate_id": candidate_id,
        "content": text,
        "embedding": emb
    }).execute()
