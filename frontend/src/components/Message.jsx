import "../styles/Message.css";

function Message({ sender, text }) {
  return (
    <div className={`message ${sender}`}>
      <div className="message-content">
        <span className="message-author">
          {sender === "user" ? "👤 Tú" : "🤖 CloudFlow Assistant"}
        </span>

        <p className="message-text">{text}</p>
      </div>
    </div>
  );
}

export default Message;
