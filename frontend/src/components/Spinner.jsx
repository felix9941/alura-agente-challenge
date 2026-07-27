import "../styles/Spinner.css";

function Spinner() {
  return (
    <div className="spinner-container">
      <div className="spinner"></div>

      <span className="spinner-text">CloudFlow Assistant está pensando...</span>
    </div>
  );
}

export default Spinner;
