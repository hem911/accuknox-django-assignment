📂 Project Structure
accuknox-django-assignment
│
├── accuknox_project/         # Django project settings
├── signals_app/              # Django signals experiments (Q1, Q2, Q3)
├── rectangles/               # Custom Rectangle class implementation
├── manage.py
└── requirements.txt

🚀 How to Run This Project
1. Create & Activate Virtual Environment

Windows
python -m venv venv
venv\Scripts\activate


Mac/Linux
python -m venv venv
source venv/bin/activate

2. Install Dependencies
pip install -r requirements.txt

3. Apply Migrations
python manage.py migrate

✅ Q1, Q2, Q3 — Django Signals Demonstration

python manage.py demo_signals
This command prints results for:

1️⃣ Are Django signals synchronous?
A handler writes to an in-memory store

The store is checked immediately after send()

Output shows handler executed before send() returned
→ Therefore, signals are synchronous by default

2️⃣ Do Django signals run in the same thread?
Caller thread ID is compared with handler thread ID
→ They are identical
→ Handlers run in the same thread

3️⃣ Do Django signals run inside the same DB transaction?
A signal handler creates a DB row inside transaction.atomic()

The caller raises an exception → forces rollback

The handler-created row does not exist after rollback
→ Handlers participate in the same transaction

🔷 Rectangle Class Demo

python manage.py demo_rectangle
This demonstrates:

Creating a Rectangle instance

Iterating over it

Showing results in required order:

{'length': <value>}
{'width': <value>}
The class is fully iterable using Python's iterator protocol.

📘 Assignment Requirements & Answers Overview
✔ Q1: Are Django signals synchronous?
Yes.
Proof: The handler executes before the send() method returns.

✔ Q2: Do Django signals run in the same thread?
Yes.
Proof: Caller thread ID == Handler thread ID.

✔ Q3: Do Django signals run in the same DB transaction?
Yes.
Proof: Handler-created database rows are rolled back when the outer transaction is rolled back.

📐 Custom Rectangle Class Requirements
Accepts length: int and width: int

Iterable

First iteration output → {'length': value}

Second iteration output → {'width': value}

All requirements are satisfied.

🙌 Notes
Project uses Django 4.2 LTS

No external libraries (except Django)

Fully runnable without modification

🧾 License
This repository is created for educational and assignment purposes for the AccuKnox Django Trainee assessment.
