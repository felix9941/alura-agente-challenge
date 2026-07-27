import "./App.css";

function App() {
  return (
    <main className="app">
      <div className="container">
        <h1>CloudFlow Assistant</h1>

        <p className="subtitle">
          Agente inteligente desarrollado con LangChain, Gemini y ChromaDB.
        </p>

        <div className="status-card">
          <h2>Backend</h2>
          <p>✅ API lista para recibir consultas.</p>
        </div>

        <div className="status-card">
          <h2>Frontend</h2>
          <p>La interfaz del chat será implementada en el siguiente commit.</p>
        </div>
      </div>
    </main>
  );
}

export default App;
