Dev Projects
A collection of small, focused projects built between 2023 and 2025. Each project is designed to be simple to run locally, practical, and close to real-world automation or analytics tasks.
⚡ Quick Start (All Projects)
Below are the exact commands to run each project locally.
Copy only the commands you need.
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
Zypher AI Automation Suite (Multi-Agent Demo)
cd zypher-ai
python3 -m http.server 3002
Open http://localhost:3002
Smart Inventory Tracker (Console Application)
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


How to Run
cd ai-call-analytics-dashboard
python3 -m http.server 3000
Open http://localhost:3000
How to Test
Inside data/data.json, change values such as:
• totalCalls
• successfulConfirmations
• reschedules
• dailyCalls
Refresh the browser — charts update instantly.
2. Password Strength Auditor (2024)
A small browser-based password auditor that scores password strength, explains weaknesses, and suggests stronger alternatives. Everything runs locally — nothing is sent anywhere.
Screenshots


How to Run
cd password-strength-auditor
python3 -m http.server 3001
Open http://localhost:3001
Test With These Example Passwords
Very weak: password
Strong: Summer2024!
Very strong: Zypher!AI_9021#24
You should see:
• Strength label
• Score
• Weakness breakdown
• Suggested variants
3. Email Summariser & Action Extractor (2024)
A Flask-based tool that summarises long emails and extracts clearer action points. Ideal for work or study.
Screenshot
How to Run
cd email-summariser-action-extractor
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python3 app.py
Open http://127.0.0.1:5000
Features
• Clean summary
• Action points
• No data is uploaded — fully local
4. Zypher AI – Automation Suite (2025)
A multi-agent automation demo showcasing three fictional AI agents:
• Appointment Agent
• Lead Qualification Agent
• Call Analytics
Screenshots



How to Run
cd zypher-ai
python3 -m http.server 3002
Open http://localhost:3002
How to Test
Click each agent on screen and watch the JSON output response appear in real time.
5. Smart Inventory Tracker (2024)
A console-based Python program that calculates days remaining before stock runs out, and flags items that need reordering.
Screenshot
How to Run
cd smart-inventory-tracker
python3 inventory_tracker.py
What It Shows
• Item
• Quantity
• Daily usage
• Days left
• Status (OK / Low / Critical)
• A list of warnings at the bottom
Folder Structure
Each project sits in its own folder so you can explore, test, and modify them independently.
Editing This README
You can update this README directly in VS Code:
Open README.md
Edit normally
Save the file
Then run:
git add README.md
git commit -m "Update README"
git push origin main
Or if you want everything staged automatically:
git add . && git commit -m "Update README" && git push origin main
