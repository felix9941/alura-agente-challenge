# --- Etapa de Build ---
FROM node:22 AS builder

WORKDIR /app

COPY package*.json ./
RUN npm install

COPY . .

ARG VITE_API_URL
ENV VITE_API_URL=${VITE_API_URL}
RUN echo "API URL = $VITE_API_URL"
RUN npm run build

# --- Etapa de Producción ---
FROM node:22-alpine

WORKDIR /app

# Instalamos el paquete 'serve' globalmente para poder usar el comando
RUN npm install -g serve

# Copiamos la carpeta 'dist' generada en la etapa anterior
COPY --from=builder /app/dist ./dist

# Exponemos el puerto estándar
EXPOSE 8080

# Ejecutamos serve dinámicamente en el puerto que Google asigne
CMD ["sh", "-c", "serve -s dist -l ${PORT:-8080}"]