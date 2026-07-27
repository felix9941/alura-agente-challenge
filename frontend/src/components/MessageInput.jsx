import { useState } from "react";
import "../styles/MessageInput.css";

function MessageInput({ onSend, loading }) {
  const [question, setQuestion] = useState("");

  const handleSubmit = () => {
    const text = question.trim();

    if (!text || loading) return;

    onSend(text);

    setQuestion("");
  };

  const handleKeyDown = (event) => {
    if (event.key === "Enter") {
      event.preventDefault();

      handleSubmit();
    }
  };

  return (
    <div className="message-input-container">
      <input
        type="text"
        className="message-input"
        placeholder="Escribe una pregunta..."
        value={question}
        onChange={(e) => setQuestion(e.target.value)}
        onKeyDown={handleKeyDown}
        disabled={loading}
      />

      <button
        className="send-button"
        onClick={handleSubmit}
        disabled={loading || !question.trim()}
      >
        {loading ? "Enviando..." : "Enviar"}
      </button>
    </div>
  );
}

export default MessageInput;
