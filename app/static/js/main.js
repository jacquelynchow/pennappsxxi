// script for speech-to-text using WebSpeech API
// reference tutorial: https://www.twilio.com/blog/speech-recognition-browser-web-speech-api

window.addEventListener("DOMContentLoaded", () => {
  const button = document.getElementById("mic");
  const result = document.getElementById("result");
  const main = document.getElementsByTagName("main")[0];
  let listening = false;
  const SpeechRecognition =
    window.SpeechRecognition || window.webkitSpeechRecognition;
  // check if browser supports WebSpeech
  if (typeof SpeechRecognition !== "undefined") {
    const recognition = new SpeechRecognition();

    const stop = () => {
      // stop listening
      recognition.stop();
      // add a class to change styles of btn recording stops
      mic = document.getElementById("mic");
      mic.classList.remove("recording");

      // set the text area to have the recorded transcript
      document.getElementById("entry-area").value += result.innerText
    };

    const start = () => {
      // start listening
      recognition.start();
      // add a class to change styles of btn when recording
      mic = document.getElementById("mic");
      mic.classList.add("recording");
    };

    const onResult = event => {
      result.innerHTML = "";
      // event.results contains transcript of speech
      for (const res of event.results) {
        const text = document.createTextNode(res[0].transcript);
        const p = document.createElement("p");
        if (res.isFinal) {
          p.classList.add("final");
        }
        // display the transcript text
        p.appendChild(text);
        result.appendChild(p);
      }
    };

    // keeps listening until we press the btn again
    recognition.continuous = true;
    // shows results as we speak
    recognition.interimResults = true;
    recognition.addEventListener("result", onResult);
    button.addEventListener("click", event => {
      listening ? stop() : start();
      listening = !listening;
    });
  } else {
    button.remove();
    const message = document.getElementById("message");
    message.removeAttribute("hidden");
    message.setAttribute("aria-hidden", "false");
  }
});
