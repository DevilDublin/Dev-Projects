fetch("data.json")
  .then((r) => r.json())
  .then((data) => {
    const total = data.totalCalls || 0;
    const confirmed = data.successfulConfirmations || 0;

    document.getElementById("total-calls").textContent = total;
    document.getElementById("confirmed").textContent = confirmed;
    document.getElementById("reschedules").textContent =
      data.reschedules ?? "–";
    document.getElementById("no-answers").textContent =
      data.noAnswers ?? "–";
    document.getElementById("avg-duration").textContent =
      data.averageCallDuration ?? "–";

    const rate = total > 0 ? Math.round((confirmed / total) * 100) : 0;
    document.getElementById("confirmed-rate").textContent = rate + "%";

    document.getElementById("raw").textContent = JSON.stringify(
      data,
      null,
      2
    );

    // Basic bar chart using plain divs
    const chart = document.getElementById("bar-chart");
    const daily = data.dailyCalls || data.dailyChart || [];
    const max = daily.length ? Math.max(...daily) : 0;

    chart.innerHTML = "";
    daily.forEach((value, index) => {
      const bar = document.createElement("div");
      bar.className = "bar";
      const height = max ? (value / max) * 100 : 0;
      bar.style.height = `${height}%`;

      const label = document.createElement("div");
      label.className = "bar-label";
      label.textContent = value;

      const day = document.createElement("div");
      day.className = "bar-day";
      day.textContent = "D" + (index + 1);

      bar.appendChild(label);
      bar.appendChild(day);
      chart.appendChild(bar);
    });
  })
  .catch(() => {
    document.getElementById("raw").textContent =
      "Could not load data.json – check that a local server is running in this folder.";
  });
