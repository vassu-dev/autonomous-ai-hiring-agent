from openai import OpenAI
from app.config import OPENAI_API_KEY

client = OpenAI(api_key=OPENAI_API_KEY)

def adaptive_question(answer):
    prompt = f"Generate next technical question based on: {answer}"
    res = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )
    return res.choices[0].message.content

def evaluate(q, a):
    prompt = f"""
    Evaluate:
    Q: {q}
    A: {a}

    Return JSON: score(0-10), feedback
    """

    res = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )
    return res.choices[0].message.content
