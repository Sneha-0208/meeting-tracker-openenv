def grade(tasks, expected):
    score = 0.0
    total = len(expected)

    for exp in expected:
        for t in tasks:
            if exp["description"] in t.description.lower():
                score += 0.5
                if "owner" in exp and t.owner == exp["owner"]:
                    score += 0.5

    return min(score / total, 1.0)