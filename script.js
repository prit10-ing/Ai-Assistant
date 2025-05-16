const recognition = new (window.SpeechRecognition || window.webkitSpeechRecognition)();
recognition.lang = 'en-US';


const synth = window.speechSynthesis;

function speak(text) {
    const utterance = new SpeechSynthesisUtterance(text);
    utterance.voice = synth.getVoices().find(voice => voice.name.includes('Female')) || synth.getVoices()[0];
    synth.speak(utterance);
}

function startListening() {
    recognition.start();
    speak("I am listening. Please say a command.");

    recognition.onresult = (event) => {
        const command = event.results[0][0].transcript.toLowerCase();
        console.log("Command:", command);
        speak(`You said: ${command}`);
        sendCommandToServer(command);
    };

    recognition.onerror = (event) => {
        console.error("Error:", event.error);
        speak("Sorry, I did not catch that. Please try again.");
    };
}

function sendCommandToServer(command) {
    fetch('http://127.0.0.1:5000/process-command', {  // Ensure correct server URL
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ command: command })
    })
    .then(response => response.json())
    .then(data => speak(data.message))
    .catch(error => {
        console.error("Error:", error);
        speak("There was an error processing your request.");
    });
}

document.getElementById("start-btn").addEventListener("click", startListening);
