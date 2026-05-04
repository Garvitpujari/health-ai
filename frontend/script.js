async function predict() {
  const res = await fetch('http://127.0.0.1:5000/predict', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({ age: 25 })
  });

  const data = await res.json();
  document.getElementById("result").innerText =
    `Risk: ${data.risk} (Confidence: ${data.confidence})`;
}
