📌 Dev Projects
A collection of small, focused projects built between 2023 and 2025.
Each project is simple to run locally, practical, and close to real-world automation or analytics tasks.
This README explains what each project does, how to run it, and includes screenshots showing the tools in action.
⚡ Quick Start (All Projects)
Copy only the line you need:
AI Call Analytics Dashboard
cd ai-call-analytics-dashboard
python3 -m http.server 3000
Open http://localhost:3000
Password Strength Auditor
cd password-strength-auditor
python3 -m http.server 3001
Open http://localhost:3001
Email Summariser & Action Extractor (Flask)
cd email-summariser-action-extractor
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python3 app.py
Open http://127.0.0.1:5000
Zypher AI – Automation Suite (Multi-Agent Demo)
cd zypher-ai
python3 -m http.server 3002
Open http://localhost:3002
Smart Inventory Tracker (Console App)
cd smart-inventory-tracker
python3 inventory_tracker.py
1. AI Call Analytics Dashboard (2025)
A lightweight browser dashboard for viewing call outcomes from AI voice agents.
It visualises:
• Total calls
• Confirmations
• Reschedules
• No answers
• Average call duration
• Daily call counts (bar chart)
Screenshots
analytics_overview.png
analytics_calls_per_day.png
analytics_raw_json.png
How to Run
cd ai-call-analytics-dashboard
python3 -m http.server 3000
Then open: http://localhost:3000
How to Test
Inside data/data.json, change values such as:
• totalCalls
• successfulConfirmations
• reschedules
• dailyCalls
Refresh the browser — charts update instantly.
2. Password Strength Auditor (2024)
A browser-based password analyser that scores strength, explains weaknesses, and suggests stronger alternatives.
Everything runs locally — nothing is ever uploaded.
Screenshots
password_strong.png
password_weak.png
password_very_strong.png
How to Run
cd password-strength-auditor
python3 -m http.server 3001
Then open: http://localhost:3001
Test Using These Example Passwords
Very weak: password
Strong: Summer2024!
Very strong: Zypher!AI_9021#24
You should see:
• Strength label
• Score
• Weakness breakdown
• Suggested variants
3. Email Summariser & Action Extractor (2024)
A Flask-based tool that summarises long emails and extracts clear action items.
Ideal for work, study or customer communication.
Screenshot
email_summariser_output.png
How to Run
cd email-summariser-action-extractor
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python3 app.py
Open: http://127.0.0.1:5000
What It Shows
• Clean summary
• Action points
• No data is uploaded — fully local
4. Zypher AI – Automation Suite (2025)
A multi-agent automation demo showcasing three fictional AI agents:
• Appointment Agent
• Lead Qualification Agent
• Call Analytics
Screenshots
zypher_agents_home.png
zypher_agent_lead_qualification.png
zypher_agent_appointment_confirmation.png
zypher_agent_call_analytics.png
How to Run
cd zypher-ai
python3 -m http.server 3002
Then open: http://localhost:3002
How to Test
Click each agent:
• Appointment Agent → Confirmation / reschedule JSON
• Lead Qualification Agent → Score + reasoning
• Call Analytics → Charts + summary
Watch the JSON output update in real time.
5. Smart Inventory Tracker (2024)
A console-based Python tool that calculates days remaining before stock runs out, and flags items that need attention.
Screenshot
inventory_console_output.png
How to Run
cd smart-inventory-tracker
python3 inventory_tracker.py
What It Shows
• Item
• Quantity
• Daily usage
• Days left
• Status (OK / Low / Critical)
• Warning messages for low-stock items
