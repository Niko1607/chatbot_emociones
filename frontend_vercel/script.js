const chatBox = document.getElementById("chat-box");
const userInput = document.getElementById("user-input");
const sendBtn = document.getElementById("send-btn");

sendBtn.addEventListener("click", enviarMensaje);
userInput.addEventListener("keypress", (e) => {
  if (e.key === "Enter") enviarMensaje();
});

async function enviarMensaje() {
  const mensaje = userInput.value.trim();
  if (!mensaje) return;

  agregarMensaje("user", mensaje);
  userInput.value = "";

  try {
    const res = await fetch("/api/chatbot/", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ message: mensaje }),
    });

    const data = await res.json();
    agregarMensaje("bot", data.response);

  } catch (error) {
    agregarMensaje("bot", "⚠ Error al conectar con el servidor");
  }
}

function agregarMensaje(tipo, texto) {
  const div = document.createElement("div");
  div.classList.add(tipo === "user" ? "user-message" : "bot-message");
  div.innerText = texto;
  chatBox.appendChild(div);
  chatBox.scrollTop = chatBox.scrollHeight;
}
