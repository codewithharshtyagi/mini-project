let alarmActive = false;

let audioContext;
let oscillator;
let gainNode;
let alarmTimer;


/* =====================================
   EMERGENCY ALARM
===================================== */

function toggleEmergencyAlarm() {

    if (!alarmActive) {

        startAlarm();

    } else {

        stopAlarm();

    }
}


function startAlarm() {

    alarmActive = true;

    const button =
        document.getElementById("alarmButton");

    if (button) {
        button.innerHTML = "🔇";
        button.title = "Stop Emergency Alarm";
    }


    audioContext =
        new (window.AudioContext ||
             window.webkitAudioContext)();


    oscillator =
        audioContext.createOscillator();

    gainNode =
        audioContext.createGain();


    oscillator.type = "sawtooth";

    oscillator.frequency.value = 750;

    gainNode.gain.value = 0.12;


    oscillator.connect(gainNode);

    gainNode.connect(audioContext.destination);

    oscillator.start();


    let high = false;


    alarmTimer = setInterval(function () {

        if (high) {

            oscillator.frequency.value = 750;

        } else {

            oscillator.frequency.value = 1050;

        }

        high = !high;

    }, 500);
}


/* =====================================
   STOP ALARM
===================================== */

function stopAlarm() {

    alarmActive = false;


    if (alarmTimer) {

        clearInterval(alarmTimer);

        alarmTimer = null;
    }


    if (oscillator) {

        try {

            oscillator.stop();

        } catch (error) {}

        oscillator = null;
    }


    if (audioContext) {

        audioContext.close();

        audioContext = null;
    }


    const button =
        document.getElementById("alarmButton");

    if (button) {

        button.innerHTML = "🚨";

        button.title = "Emergency Alarm";
    }
}


/* =====================================
   CHECKLIST COUNTER
===================================== */

function updateChecklist() {

    const checkboxes =
        document.querySelectorAll(
            ".check-item input"
        );

    const checked =
        document.querySelectorAll(
            ".check-item input:checked"
        ).length;


    const total = checkboxes.length;


    const counter =
        document.getElementById(
            "checkCounter"
        );


    if (counter) {

        counter.innerText =
            checked + " / " + total +
            " items completed";
    }
}
