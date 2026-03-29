# run_agent.py
from env.models import Action

# --- ASK USER FOR TICKET DESCRIPTION ---
ticket_message = input("Enter the ticket description: ")

# --- MOCK RESPONSE BASED ON KEYWORDS ---
ticket_lower = ticket_message.lower()

if "urgent" in ticket_lower or "failure" in ticket_lower or "critical" in ticket_lower:
    score_value = 1.0
    suggested_action_text = "Assign to support team immediately."
    category_value = "critical"
    priority_value = "high"
elif "slow" in ticket_lower or "issue" in ticket_lower or "problem" in ticket_lower:
    score_value = 0.7
    suggested_action_text = "Review and assign to the team."
    category_value = "performance"
    priority_value = "medium"
else:
    score_value = 0.3
    suggested_action_text = "Low priority, schedule later."
    category_value = "general"
    priority_value = "low"

# --- CREATE ACTION OBJECT (optional, for completeness) ---
action = Action(
    category=category_value,
    priority=priority_value,
    response=suggested_action_text
)

# --- PRINT OUTPUT ---
print("\n--- Ticket Triage Result ---")
print("Ticket description:", ticket_message)
print("Score:", score_value)
print("Suggested action:", suggested_action_text)
print("Category:", category_value)
print("Priority:", priority_value)