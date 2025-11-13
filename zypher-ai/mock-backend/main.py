from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional

app = FastAPI(title="Zypher AI Mock Backend")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],        
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class ConfirmRequest(BaseModel):
  leadId: str
  canAttend: bool


class RescheduleRequest(BaseModel):
  leadId: str
  requestedTimeIso: str


class ChatRequest(BaseModel):
  leadId: Optional[str] = None
  message: str


class QualificationRequest(BaseModel):
  firstName: str
  service: str


@app.post("/lead")
def get_lead():
  return {
    "leadId": "L-10294",
    "firstName": "Sophie",
    "phone": "+447912345678",
    "appointmentTimeIso": "2025-03-12T15:00:00+00:00",
    "service": "Consultation",
    "notes": "Requested reminder call."
  }


@app.post("/confirm-appointment")
def confirm_appointment(req: ConfirmRequest):
  if req.canAttend:
    status = "confirmed"
    message = "Appointment has been confirmed."
  else:
    status = "not_confirmed"
    message = "Lead could not confirm the appointment."
  return {"status": status, "message": message, "leadId": req.leadId}


@app.post("/reschedule")
def reschedule(req: RescheduleRequest):
  return {
    "status": "rescheduled",
    "newTime": req.requestedTimeIso,
    "message": "Your appointment has been rescheduled."
  }


@app.post("/chat")
def chat(req: ChatRequest):
  return {
    "reply": "Thanks for the update. I have made a note of that for you.",
    "echo": req.message
  }


@app.post("/call-summary")
def call_summary():
  return {
    "leadId": "L-10294",
    "summary": "Lead confirmed the appointment at 3 PM. No reschedule requested.",
    "sentiment": "positive",
    "durationSeconds": 64
  }


@app.get("/analytics")
def analytics():
  return {
    "totalCalls": 42,
    "successfulConfirmations": 34,
    "reschedules": 5,
    "noAnswers": 3,
    "averageCallDuration": 58,
    "dailyChart": [3, 7, 6, 5, 4, 8, 9]
  }


@app.post("/lead-qualification")
def qualify(req: QualificationRequest):
  return {
    "qualified": True,
    "score": 87,
    "reason": f"{req.firstName} requested a {req.service} and meets the basic criteria."
  }
