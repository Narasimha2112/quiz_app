let timeLeft = 120; // seconds
const timerEl = document.getElementById("timer");
const quizForm = document.getElementById("quizForm");

const formatTime = (secs) => {
    const mins = String(Math.floor(secs / 60)).padStart(2, '0');
    const seconds = String(secs % 60).padStart(2, '0');
    return `${mins}:${seconds}`;
};

const countdown = setInterval(() => {
    timeLeft--;
    timerEl.textContent = "Time Left: " + formatTime(timeLeft);

    if (timeLeft <= 0) {
        clearInterval(countdown);
        timerEl.textContent = "Time's up!";
        quizForm.submit();
    }
}, 1000);
