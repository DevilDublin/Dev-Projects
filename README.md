
Dev Projects
A collection of small, focused projects built between 2023 and 2025. Each project is simple to run locally and designed to be understandable, practical and close to real-world automation or analytics tasks.
Quick Start (All Projects)
Below are the exact commands to run each project. These are written as plain text — just copy the line you need.
AI Call Analytics Dashboard:
cd ai-call-analytics-dashboard
python3 -m http.server 3000
Open http://localhost:3000
Password Strength Auditor:
cd password-strength-auditor
python3 -m http.server 3001
Open http://localhost:3001
Email Summariser (Flask):
cd email-summariser-action-extractor
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python3 app.py
Open http://127.0.0.1:5000
Zypher AI Automation Suite:
cd zypher-ai
python3 -m http.server 3002
Open http://localhost:3002
Smart Inventory Tracker:
cd smart-inventory-tracker
python3 inventory_tracker.py
Projects
1. AI Call Analytics Dashboard (2025)
A lightweight dashboard for viewing call outcomes from AI voice agents, including confirmations, reschedules, average duration and daily call counts.
Screenshots
(Your images)
analytics_overview.png
analytics_calls_per_day.png
analytics_raw_json.png
How to Run
cd ai-call-analytics-dashboard
python3 -m http.server 3000
Open in browser:
http://localhost:3000
How to Test
Change the values inside data/data.json, such as:
totalCalls
successfulConfirmations
reschedules
dailyCalls
Refresh the browser — the cards and green bar chart update instantly.
2. Password Strength Auditor (2024)
A browser-based password analyser that scores strength, explains weaknesses and suggests stronger, realistic alternatives. Everything runs locally.
Screenshots
password_strong.png
password_weak.png
password_very_strong.png
How to Run
cd password-strength-auditor
python3 -m http.server 3001
Open http://localhost:3001
How to Test
Try these example passwords:
Very weak:
password
Strong:
Summer2024!
Very strong:
Zypher!AI_9021#24
You should see:
Strength label
Score
Weakness breakdown
Suggested variants
3. Email Summariser & Action Extractor (2024)
A Flask-based tool that summarises long emails and extracts clear action items. Ideal for work or study.
Screenshot
email_summariser_output.png
How to Run
cd email-summariser-action-extractor
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python3 app.py
Open in browser:
http://127.0.0.1:5000
How to Test
Paste any long email (work, uni, etc.) and click “Summarise Email”.
You should get:
A clean, readable summary
Bullet-point action items
4. Zypher AI – Automation Suite (2025)
A front-end showcase of:
Appointment confirmation agent
Lead qualification agent
Call analytics viewer
Screenshots
zypher_agents_home.png
zypher_agent_lead_qualification.png
zypher_agent_call_analytics.png
zypher_agent_appointment_confirmation.png
How to Run
cd zypher-ai
python3 -m http.server 3002
Open http://localhost:3002
How to Test
Click the buttons:
Preview Agent (Appointment)
Preview Agent (Lead Qualification)
View Analytics
The output panel on the right should update with:
Confirmation / reschedule messages
Qualification score + reasoning
Analytics JSON with call stats
5. Smart Inventory Tracker (2024)
A command-line tool that examines stock levels, calculates remaining days and flags low/critical items.
Screenshot
inventory_tracker_output.png
How to Run
cd smart-inventory-tracker
python3 inventory_tracker.py
How to Test
Edit the file inventory.csv and change some numbers, for example:
Coffee beans, 30, 5
USB cables, 2, 4
Printer paper, 300, 5
Re-run the script.
You’ll see:
Updated days left
Items marked Low or Critical
Warnings printed beneath the table
