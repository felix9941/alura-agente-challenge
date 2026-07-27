import { useState, useRef, useEffect } from "react";
import Message from "./Message";
import MessageInput from "./MessageInput";
import Spinner from "./Spinner";
import { askQuestion } from "../services/api";
import "../styles/Chat.css";

const Chat = () => {
  const [messages, setMessages] = useState([]);
  const [isTyping, setIsTyping] = useState(false);

  // Referencia para mantener el scroll siempre abajo
  const messagesEndRef = useRef(null);

  const scrollToBottom = () => {
    messagesEndRef.current?.scrollIntoView({ behavior: "smooth" });
  };

  useEffect(() => {
    scrollToBottom();
  }, [messages, isTyping]);

  const handleSendMessage = async (text) => {
    if (!text.trim()) return;

    // 1. Agregamos el mensaje del usuario a la vista
    const newUserMessage = { sender: "user", text };
    setMessages((prev) => [...prev, newUserMessage]);

    // 2. Activamos el spinner
    setIsTyping(true);

    try {
      // 3. Enviamos la consulta al backend
      const response = await askQuestion(text);
      const botText =
        response.respuesta ||
        response.answer ||
        "No se recibió una respuesta clara del servidor.";

      const newBotMessage = { sender: "bot", text: botText };
      setMessages((prev) => [...prev, newBotMessage]);
    } catch (error) {
      const errorMessage = { sender: "bot", text: `⚠️ ${error.message}` };
      setMessages((prev) => [...prev, errorMessage]);
    } finally {
      setIsTyping(false);
    }
  };

  return (
    <div className="chat-wrapper">
      <div className="chat-container">
        <header className="chat-header">
          <h2>Alura Agente Corporativo</h2>
          <span className="status-indicator">
            <span className="dot online"></span> En línea
          </span>
        </header>

        <div className="chat-messages">
          {messages.length === 0 && (
            <div className="chat-empty-state">
              <div className="empty-icon">🤖</div>
              <h3>¡Hola! Soy tu asistente.</h3>
              <p>
                Puedes hacerme preguntas sobre los documentos, políticas y bases
                de conocimiento de la empresa.
              </p>
            </div>
          )}

          {messages.map((msg, index) => (
            <Message key={index} sender={msg.sender} text={msg.text} />
          ))}

          {isTyping && (
            <div className="chat-typing-indicator">
              <Spinner />
              <span>Analizando documentos...</span>
            </div>
          )}
          <div ref={messagesEndRef} />
        </div>

        <div className="chat-input-section">
          <MessageInput onSendMessage={handleSendMessage} disabled={isTyping} />
        </div>
      </div>
    </div>
  );
};

export default Chat;
