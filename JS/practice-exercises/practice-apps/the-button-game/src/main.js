// -------------------------------
// Declarations
// -------------------------------
let startButton,
  pauseButton,
  timer,
  timerInterval,
  isRunning = false,
  points = 0,
  progress,
  progressCount,
  pointButton,
  totalSeconds = 0;

startButton = document.getElementById("play");
progressCount = document.getElementById("progress-count");
pointButton = document.getElementById("point-button");
progress = document.getElementById("progress");
pauseButton = document.getElementById("pause");
timer = document.getElementById("timer");
timer.innerHTML = "30";
progressCount.innerHTML = "0/5 clicked";
progress.style = "background: none;";

// -------------------------------
// Functions
// -------------------------------
function setTime() {
  ++totalSeconds;
  timer.innerHTML = pad(totalSeconds % 60);
  pointButton.disabled = false;
  if (totalSeconds > 30) {
    alert("you lost");
    reset();
  }
}

function pad(val) {
  let valString = val + "";
  if (valString.length < 2) {
    return 30 - valString;
  } else {
    return 30 - valString;
  }
}

function reset() {
  points = 0;
  totalSeconds = 0;
  timer.innerHTML = "30";
  progressCount.innerHTML = `${points}/5 clicked`;
  progress.style = `background: none;`;
  pointButton.disabled = true;
  startButton.disabled = false;
  pauseButton.disabled = true;
  clearInterval(timerInterval);
}

function start() {
  startButton.addEventListener("click", () => {
    timerInterval = setInterval(setTime, 1000);
    startButton.disabled = true;
    pauseButton.disabled = false;
    pointButton.disabled = false;
  });
  pauseButton.addEventListener("click", () => {
    clearInterval(timerInterval);
    pointButton.disabled = true;
    pauseButton.disabled = true;
    startButton.disabled = false;
  });
  pointButton.addEventListener("click", () => {
    points += 1;
    progressCount.innerHTML = `${points}/5 clicked`;
    progress.style = `background: linear-gradient(
        to right,
    var(--green) 0%,
    var(--green) ${points * 20}%,
    #fff 20%,
    #fff 100%);`;
    if (points === 5) {
      alert("you won");
      reset();
    }
    pointButton.style = `top: ${Math.floor(Math.random() * 90) +
      1}%; left: ${Math.floor(Math.random() * 60) + 1}%`;
  });
  pauseButton.disabled = true;
  pointButton.disabled = true;
}

start();
