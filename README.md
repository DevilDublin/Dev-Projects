# Dev Projects

This repository is a collection of small, focused developer projects. Each project is designed to be practical, easy to run locally, and demonstrates a specific task in analytics, automation, or web development using Python, Flask, and vanilla HTML/CSS/JavaScript.

## Projects Overview

| Project                                 | Description                                                                  | Technologies                     |
| --------------------------------------- | ---------------------------------------------------------------------------- | -------------------------------- |
| **AI Call Analytics Dashboard**         | A static dashboard for visualizing call center AI agent performance.         | HTML, CSS, Vanilla JS            |
| **Email Summariser & Action Extractor** | A Flask app that summarizes emails and extracts actionable tasks.            | Python, Flask                    |
| **Password Strength Auditor**           | A web-based tool to score password strength and suggest improvements.        | Python, Flask                    |
| **Smart Inventory Tracker**             | A command-line utility to forecast stock depletion based on usage.           | Python (standard library)        |
| **Zypher AI - Automation Suite**        | A UI demo for a multi-agent AI system with a mock FastAPI backend.           | HTML, JS, Python, FastAPI        |

---

## 1. AI Call Analytics Dashboard

A lightweight, browser-based dashboard for viewing call outcomes from AI voice agents. It visualizes key performance metrics from a `data.json` file.

### Features
- **Key Metrics:** Displays total calls, confirmations, reschedules, and no-answers.
- **Confirmation Rate:** Calculates and shows the percentage of successful confirmations.
- **Call Duration:** Shows the average call duration in seconds.
- **Daily Trends:** A bar chart visualizes the number of calls handled per day.
- **Raw Data View:** Includes a section to display the raw JSON payload being used.

### How to Run
1. Navigate to the project directory:
   ```sh
   cd ai-call-analytics-dashboard
   ```
2. Start a simple Python web server:
   ```sh
   python3 -m http.server 3000
   ```
3. Open your browser to `http://localhost:3000`.

To test, you can modify the values in `data.json` and refresh the page to see the dashboard update.

---

## 2. Email Summariser & Action Extractor

A Flask-based web tool that takes long email text as input, provides a concise one-sentence summary, and extracts a clear list of action items.

### Features
- **AI-Free Logic:** Uses a rule-based system with keywords (`fix`, `send`, `review`) and request triggers (`can you`, `we need to`) to identify tasks.
- **Clean Output:** Presents a simple summary and a bulleted list of action points.
- **Local Processing:** All text is processed locally in the Flask backend; no data is sent to external services.

### How to Run
1. Navigate to the project directory:
   ```sh
   cd email-summariser-action-extractor
   ```
2. Create and activate a virtual environment:
   ```sh
   python3 -m venv venv
   source venv/bin/activate
   # On Windows, use: venv\Scripts\activate
   ```
3. Install the required dependencies:
   ```sh
   pip install -r requirements.txt
   ```
4. Run the Flask application:
   ```sh
   python3 app.py
   ```
5. Open your browser to `http://127.0.0.1:5000`.

---

## 3. Password Strength Auditor

A simple security tool that scores password strength, explains its weaknesses, and suggests stronger alternatives. The analysis is performed entirely in the browser and backend, with nothing ever being uploaded.

### Features
- **Strength Scoring:** Rates passwords as "Very Weak," "Strong," etc., based on a scoring system.
- **Weakness Analysis:** Provides specific reasons for a low score, such as being too short, lacking character variety, or matching a common password.
- **Suggestions:** Generates stronger, memorable variants of the input password.
- **Local Auditing:** Reads from `common_passwords.txt` for common password checks.

### How to Run
1. Navigate to the project directory:
   ```sh
   cd password-strength-auditor
   ```
2. Create and activate a virtual environment:
   ```sh
   python3 -m venv venv
   source venv/bin/activate
   # On Windows, use: venv\Scripts\activate
   ```
3. Install the required dependencies:
   ```sh
   pip install -r requirements.txt
   ```
4. Run the Flask application:
   ```sh
   python3 app.py
   ```
5. Open your browser to `http://127.0.0.1:5000`.

---

## 4. Smart Inventory Tracker

A console-based Python script that calculates the remaining days before stock runs out and flags items that need reordering.

### Features
- **CSV Input:** Reads item data from `inventory.csv`, including current quantity and average daily usage.
- **Depletion Forecasting:** Calculates the "Days Left" for each item.
- **Status Flagging:** Assigns a status (`OK`, `Low`, `Critical`) based on the forecast.
- **Actionable Warnings:** Prints a summary of warnings for items with low or critical stock levels.

### How to Run
1. Navigate to the project directory:
   ```sh
   cd smart-inventory-tracker
   ```
2. Run the script from your terminal:
   ```sh
   python3 inventory_tracker.py
   ```
### Example Output
```
 SMART INVENTORY TRACKER — CONSOLE VIEW
 -------------------------------------

Item                    Qty    Daily usage   Days left  Status      
----------------------------------------------------------------------
Coffee beans            30     5             6          Low         
Printer paper           200    12            16.6       OK          
Bottled water           15     3             5          Low         
USB cables              8      4             2          Critical    
Phone cases             5      2             2.5        Critical    

Warnings:
- Coffee beans: Should be reordered soon
- Bottled water: Should be reordered soon
- USB cables: Running critically low
- Phone cases: Running critically low
```

---

## 5. Zypher AI - Automation Suite

A frontend demo for a fictional multi-agent AI automation platform. The interface allows you to simulate calls to different AI agents and view the mock JSON responses from a FastAPI backend.

### Features
- **Agent Simulation:** Provides a UI to interact with three demo agents: Appointment Agent, Lead Qualification Agent, and Call Analytics.
- **Frontend-Backend Interaction:** The vanilla JavaScript frontend makes API calls to a local mock backend.
- **Mock API:** The backend is built with FastAPI and serves realistic JSON responses for different agent tasks.

### How to Run
This project requires running two separate processes in two terminal windows.

**Terminal 1: Run the Backend**
1. Navigate to the backend directory:
   ```sh
   cd zypher-ai/mock-backend
   ```
2. Install the required dependencies:
   ```sh
   pip install -r requirements.txt
   ```
3. Start the FastAPI server with Uvicorn:
   ```sh
   uvicorn main:app --reload
   ```
   The backend will be running at `http://127.0.0.1:8000`.

**Terminal 2: Run the Frontend**
1. Navigate to the frontend directory:
   ```sh
   cd zypher-ai/frontend
   ```
2. Start a simple Python web server:
   ```sh
   python3 -m http.server 3000
   ```
3. Open your browser to `http://localhost:3000`. Click on the agent cards to see the JSON output from the backend.
