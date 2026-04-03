from app.database import update_weights

def learn(top_candidates):
    avg_exp = sum(c["experience"] for c in top_candidates) / len(top_candidates)

    if avg_exp > 2:
        w = {"skill": 0.3, "experience": 0.5, "resume": 0.2}
    else:
        w = {"skill": 0.5, "experience": 0.3, "resume": 0.2}

    update_weights(w)
