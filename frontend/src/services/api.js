import axios from "axios";
const api = axios.create({
  baseURL: import.meta.env.VITE_API_URL,
  headers: {
    "Content-Type": "application/json",
  },
  timeout: 400000,
});
/**
 * Envía una pregunta al agente RAG.
 *
 * @param {string} question
 * @returns {Promise<Object>}
 */
export async function askQuestion(question) {
  try {
    const response = await api.post("/chat", {
      question,
    });

    return response.data;
  } catch (error) {
    console.error("Error al consultar la API:", error);

    if (error.response) {
      throw new Error(error.response.data.detail || "Error del servidor.", {
        cause: error,
      });
    }

    if (error.request) {
      throw new Error("No fue posible conectar con el servidor.", {
        cause: error,
      });
    }

    throw new Error("Ocurrió un error inesperado.", { cause: error });
  }
}

export default api;
