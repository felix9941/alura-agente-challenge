import ReactMarkdown from "react-markdown";
import "../styles/Message.css";

function Message({ sender, text }) {
  return (
    <div className={`message ${sender}`}>
      <div className="message-content">
        <span className="message-author">
          {sender === "user" ? "👤 Tú" : "🤖 CloudFlow Assistant"}
        </span>

        <div className="message-text">
          <ReactMarkdown>{text}</ReactMarkdown>
        </div>
      </div>
    </div>
  );
}

export default Message;
