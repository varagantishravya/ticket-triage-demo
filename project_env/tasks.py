import random

tasks = [
    {
        "ticket_id": 1,
        "message": "I was charged twice for my subscription",
        "customer_type": "premium",
        "correct_category": "billing",
        "correct_priority": "high"
    },
    {
        "ticket_id": 2,
        "message": "App is crashing when I open it",
        "customer_type": "free",
        "correct_category": "technical",
        "correct_priority": "medium"
    },
    {
        "ticket_id": 3,
        "message": "How do I change my email?",
        "customer_type": "free",
        "correct_category": "general",
        "correct_priority": "low"
    }
]

def get_task():
    return random.choice(tasks)