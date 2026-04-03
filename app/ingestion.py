import random

def fetch_candidates():
    skills = ["Java", "React", "Node", "Python", "SQL"]

    return [
        {
            "name": f"Candidate_{i}",
            "skills": random.sample(skills, 2),
            "experience": random.randint(0, 4),
            "resume": "Strong developer with practical experience"
        }
        for i in range(1000)
    ]
