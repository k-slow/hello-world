"""
Deterministic generator for the demo dataset: 100 synthetic collections contacts.

Run:  python3 gen_data.py
Writes: data/contacts.json  (100 rows)

Nothing here is real PII -- names/phones are fabricated and seeded so the dataset
is reproducible. The fields are the ones a real contact-eligibility / NLC engine
needs to make a "can we legally contact this person right now?" decision.
"""
import json
import os
import random

random.seed(42)

FIRST = ["James", "Maria", "Robert", "Linda", "David", "Patricia", "John", "Jennifer",
         "Michael", "Elizabeth", "William", "Susan", "Richard", "Jessica", "Joseph",
         "Sarah", "Thomas", "Karen", "Carlos", "Nancy", "Daniel", "Lisa", "Matthew",
         "Betty", "Anthony", "Sandra", "Mark", "Ashley", "Steven", "Kimberly"]
LAST = ["Smith", "Johnson", "Williams", "Brown", "Jones", "Garcia", "Miller", "Davis",
        "Rodriguez", "Martinez", "Hernandez", "Lopez", "Gonzalez", "Wilson", "Anderson",
        "Thomas", "Taylor", "Moore", "Jackson", "Martin", "Lee", "Perez", "Thompson",
        "White", "Harris", "Sanchez", "Clark", "Ramirez", "Lewis", "Robinson"]

# (state, timezone label, default area code) -- mix of strict and normal states
STATES = [
    ("NY", "America/New_York", "212"),   # strict mini-TCPA
    ("FL", "America/New_York", "305"),   # Florida Telephone Solicitation Act (strict)
    ("TX", "America/Chicago", "214"),
    ("CA", "America/Los_Angeles", "415"),
    ("UT", "America/Denver", "801"),
    ("IL", "America/Chicago", "312"),
    ("GA", "America/New_York", "404"),
    ("WA", "America/Los_Angeles", "206"),
    ("OK", "America/Chicago", "405"),    # Oklahoma mini-TCPA (strict)
    ("AZ", "America/Phoenix", "602"),
]

CONSENT = ["written", "verbal", "none", "revoked"]
CONSENT_W = [0.30, 0.25, 0.30, 0.15]


def make_phone(area):
    return f"({area}) {random.randint(200,999)}-{random.randint(1000,9999)}"


contacts = []
for i in range(1, 101):
    state, tz, area = random.choice(STATES)
    consent = random.choices(CONSENT, weights=CONSENT_W)[0]
    local_hour = random.randint(6, 22)
    contacts.append({
        "id": f"C{i:03d}",
        "name": f"{random.choice(FIRST)} {random.choice(LAST)}",
        "phone": make_phone(area),
        "state": state,
        "timezone": tz,
        "consent": consent,
        "on_national_dnc": random.random() < 0.35,
        "on_internal_dnc": random.random() < 0.08,
        "is_known_litigator": random.random() < 0.05,
        "reassigned_risk": random.random() < 0.07,
        "attempts_last_7d": random.choices([0, 1, 2, 3, 5, 7, 9],
                                           weights=[25, 25, 20, 12, 8, 6, 4])[0],
        "last_contact_days_ago": random.choice([0, 1, 2, 4, 8, 15, 30, 90]),
        "local_hour": local_hour,
        "debt_id": f"D{random.randint(10000,99999)}",
        "balance": round(random.uniform(120, 9800), 2),
    })

os.makedirs(os.path.join(os.path.dirname(__file__), "data"), exist_ok=True)
out = os.path.join(os.path.dirname(__file__), "data", "contacts.json")
with open(out, "w") as f:
    json.dump(contacts, f, indent=2)

print(f"Wrote {len(contacts)} contacts -> {out}")
