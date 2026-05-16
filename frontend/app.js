let history = [];
let round = 1;

document.getElementById("startBtn").addEventListener("click", async () => {
  const res = await fetch("http://127.0.0.1:8000/start");
  const data = await res.json();

  document.getElementById("scenario").innerHTML = `
    <h3>📜 Scenario</h3>
    <p>${data.scenario}</p>
  `;

  round = data.round;
  history = [];
  document.getElementById("battleLog").innerHTML = "";
});


document.getElementById("submitBtn").addEventListener("click", async () => {
  const solution = document.getElementById("solution").value;

  const res = await fetch("http://127.0.0.1:8000/submit", {
    method: "POST",
    headers: {"Content-Type": "application/json"},
    body: JSON.stringify({ solution, history, round })
  });

  const data = await res.json();

  history.push({
    solution,
    score: data.score
  });

  // 🔥 APPEND NEW ROUND (NOT REPLACE)
  const log = document.getElementById("battleLog");

  log.innerHTML += `
    <div class="card">
      <div class="round">⚔️ Round ${round}</div>

      <div class="attack-card">
        <p>🚨 ${data.attack}</p>
        <p>🧪 ${data.edge_cases}</p>
        <p class="score">📊 Score: ${data.score}</p>

        <div class="progress-bar">
          <div class="progress" style="width:${data.score}%"></div>
        </div>
      </div>
    </div>
  `;

  round = data.round;
});