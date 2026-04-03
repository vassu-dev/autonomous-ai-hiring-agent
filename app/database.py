from supabase import create_client
from app.config import SUPABASE_URL, SUPABASE_KEY

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

def insert_candidate(c):
    supabase.table("candidates").insert(c).execute()

def get_candidates():
    return supabase.table("candidates").select("*").execute().data

def update_score(cid, score):
    supabase.table("candidates").update({"score": score}).eq("id", cid).execute()

def insert_interview(data):
    supabase.table("interviews").insert(data).execute()

def get_weights():
    return supabase.table("weights").select("*").execute().data[0]

def update_weights(w):
    supabase.table("weights").update(w).eq("id", 1).execute()
