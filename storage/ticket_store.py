import json
import os
from datetime import datetime

TICKET_FILE = "storage/tickets.json"


def save_ticket(ticket: dict):
    # Create file if it does not exist
    if not os.path.exists(TICKET_FILE):
        with open(TICKET_FILE, "w") as f:
            json.dump([], f)

    # Load existing tickets
    with open(TICKET_FILE, "r") as f:
        tickets = json.load(f)

    # Add new ticket
    tickets.append(ticket)

    # Save back
    with open(TICKET_FILE, "w") as f:
        json.dump(tickets, f, indent=4)


def create_ticket_document(issue: str, ticket_id: str):
    return {
        "ticket_id": ticket_id,
        "issue": issue,
        "status": "open",
        "created_at": datetime.utcnow().isoformat()
    }
