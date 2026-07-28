/**
 * Chat Component
 *
 * Controla la conversación entre el usuario y el asistente.
 */

import { useRef, useState, useEffect } from "react";

import "../styles/Chat.css";

import Message from "./Message";
import MessageInput from "./MessageInput";
import Spinner from "./Spinner";

import { askQuestion } from "../services/api";

function Chat() {
  const [messages, setMessages] = useState([
    {
      sender: "bot",
      text: "¡Hola! 👋 Soy CloudFlow Assistant. ¿En qué puedo ayudarte?",
    },
  ]);

  const [loading, setLoading] = useState(false);

  const messagesEndRef = useRef(null);

  /**
   * Hace scroll automático al último mensaje.
   */
  useEffect(() => {
    messagesEndRef.current?.scrollIntoView({
      behavior: "smooth",
    });
  }, [messages]);

  /**
   * Envía la pregunta al backend.
   */
  const handleSend = async (question) => {
    // Agrega mensaje del usuario
    setMessages((prev) => [
      ...prev,
      {
        sender: "user",
        text: question,
      },
    ]);

    setLoading(true);

    try {
      const response = await askQuestion(question);

      setMessages((prev) => [
        ...prev,
        {
          sender: "bot",
          text: response.answer,
        },
      ]);
    } catch (error) {
      setMessages((prev) => [
        ...prev,
        {
          sender: "bot",
          text: error.message || "Ocurrió un error al consultar el asistente.",
        },
      ]);
    }

    setLoading(false);
  };

  return (
    <div className="chat-container">
      <div className="chat-header">
        <h1>🤖 CloudFlow Assistant</h1>

        <p>Consulta la documentación de CloudFlow mediante IA.</p>
      </div>

      <div className="messages-container">
        {messages.map((message, index) => (
          <Message key={index} sender={message.sender} text={message.text} />
        ))}

        {loading && <Spinner />}

        <div ref={messagesEndRef}></div>
      </div>

      <MessageInput loading={loading} onSend={handleSend} />
    </div>
  );
}

export default Chat;
