const outputBox = document.getElementById("zy-output-box");
const cards = document.querySelectorAll(".zy-card");

const BACKEND_URL = "http://127.0.0.1:8000";

function setOutput(text, isError = false) {
  outputBox.textContent = text;
  outputBox.style.color = isError ? "#ff6b6b" : "#9fa4b5";
}

async function callEndpoint(path, payload) {
  setOutput("Talking to Zypher mock backend…");
  try {
    const res = await fetch(`${BACKEND_URL}${path}`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(payload || {})
    });
    const data = await res.json();
    setOutput(JSON.stringify(data, null, 2));
  } catch (err) {
    setOutput("Could not reach the mock backend. Is FastAPI running?", true);
  }
}

cards.forEach(card => {
  card.addEventListener("click", () => {
    const agent = card.getAttribute("data-agent");
    if (agent === "appointment") {
      callEndpoint("/confirm-appointment", {
        leadId: "L-10294",
        canAttend: true
      });
    } else if (agent === "qualification") {
      callEndpoint("/lead-qualification", {
        firstName: "Sophie",
        service: "Consultation"
      });
    } else if (agent === "analytics") {
      fetch(`${BACKEND_URL}/analytics`)
        .then(r => r.json())
        .then(data => setOutput(JSON.stringify(data, null, 2)))
        .catch(() => setOutput("Could not reach analytics endpoint.", true));
    }
  });
});
