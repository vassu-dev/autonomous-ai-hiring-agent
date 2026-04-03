from fastapi import FastAPI
from app.ingestion import fetch_candidates
from app.database import insert_candidate, get_candidates, update_score, insert_interview
from app.scoring import score_candidate
from app.ranking import rank_candidates
from app.interview import adaptive_question, evaluate
from app.ai_detection import detect
from app.learning import learn
from app.memory import store

app = FastAPI()

@app.post("/pipeline")
def pipeline():
    # ingest
    for c in fetch_candidates():
        insert_candidate(c)

    # score
    for c in get_candidates():
        s = score_candidate(c)
        update_score(c["id"], s)

    ranked = rank_candidates(get_candidates())
    top = ranked[:10]

    for c in top:
        q = "Explain OOP"
        answers = [
            "OOP uses classes",
            "REST uses HTTP",
            "Normalization reduces redundancy"
        ]

        for a in answers:
            eval_res = evaluate(q, a)
            flag = detect(a)

            insert_interview({
                "candidate_id": c["id"],
                "question": q,
                "answer": a,
                "evaluation": eval_res,
                "ai_flag": flag
            })

            store(c["id"], a)

            q = adaptive_question(a)

    learn(top)

    return {"top_candidates": top}
