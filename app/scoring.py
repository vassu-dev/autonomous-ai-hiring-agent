from openai import OpenAI
from app.config import OPENAI_API_KEY
from app.database import get_weights

client = OpenAI(api_key=OPENAI_API_KEY)

def score_candidate(c):
    w = get_weights()

    prompt = f"""
    Score candidate (0-100):

    Skills: {c['skills']}
    Experience: {c['experience']}
    Resume: {c['resume']}

    Weight skills={w['skill']}, experience={w['experience']}, resume={w['resume']}
    """

    res = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    return float(res.choices[0].message.content.strip())
