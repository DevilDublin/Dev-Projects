fetch("data.json")
  .then(r => r.json())
  .then(data => {
    document.getElementById("total-calls").textContent = data.totalCalls;
    document.getElementById("confirmed").textContent = data.successfulConfirmations;
    document.getElementById("reschedules").textContent = data.reschedules;
    document.getElementById("no-answers").textContent = data.noAnswers;
    document.getElementById("raw").textContent = JSON.stringify(data, null, 2);
  })
  .catch(() => {
    document.getElementById("raw").textContent = "Could not load data.json";
  });
