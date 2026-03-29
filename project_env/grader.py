def grade_action(task, action):
    score = 0.0

    # Category check
    if action.category == task["correct_category"]:
        score += 0.5
    else:
        score -= 0.2

    # Priority check
    if action.priority == task["correct_priority"]:
        score += 0.3

    # Response quality (simple check)
    if len(action.response) > 20:
        score += 0.2

    return max(0.0, min(1.0, score)), "Evaluation complete"