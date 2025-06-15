let currentInput = "";

function appendValue(value) {
  const lastChar = currentInput.slice(-1);

  const operators = ['+', '-', '*', '/'];
  if (operators.includes(value) && operators.includes(lastChar)) {
    return;
  }

  if (value === '.' && lastChar === '.') {
    return;
  }

  currentInput += value;
  updateDisplay();
}

function clearDisplay() {
  currentInput = "";
  updateDisplay();
}

function backspace() {
  currentInput = currentInput.slice(0, -1);
  updateDisplay();
}

function calculate() {
  try {
    if (currentInput.includes("/0")) {
      document.getElementById("display").innerText = "Error";
      currentInput = "";
      return;
    }
    const result = eval(currentInput);
    currentInput = result.toString();
    updateDisplay();
  } catch (e) {
    document.getElementById("display").innerText = "Error";
    currentInput = "";
  }
}

function updateDisplay() {
  document.getElementById("display").innerText = currentInput || "0";
}
document.addEventListener("keydown", function(event) {
  const key = event.key;

  if (!isNaN(key) || ['+', '-', '*', '/', '.'].includes(key)) {
    appendValue(key);
  } else if (key === "Enter") {
    calculate();
  } else if (key === "Backspace") {
    backspace();
  } else if (key.toLowerCase() === "c") {
    clearDisplay();
  }
});
function toggleTheme() {
  document.body.classList.toggle("light");

  const toggleBtn = document.getElementById("theme-toggle");
  if (document.body.classList.contains("light")) {
    toggleBtn.textContent = "🌙";
  } else {
    toggleBtn.textContent = "☀️";
  }
}
