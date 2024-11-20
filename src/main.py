from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from src.chatbot import CarTroubleshootingChatbot
import logging

# Crear instancia de FastAPI
app = FastAPI(
    title="Car Troubleshooting Chatbot API",
    description="API para diagnosticar problemas automotrices utilizando un chatbot.",
    version="1.0.0"
)

# Configurar CORS (necesario si conectas con un frontend)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Cambia "*" por el dominio de tu frontend en producción
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Inicializar el chatbot
chatbot = CarTroubleshootingChatbot()

# Configurar el registro de errores
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

# Modelo de datos para solicitudes
class Message(BaseModel):
    text: str

@app.get("/")
async def root():
    """Endpoint raíz para verificar que el servidor está activo."""
    return {"message": "Car Troubleshooting Chatbot API está activa."}

@app.post("/diagnose/")
async def diagnose(message: Message):
    """
    Procesa un mensaje enviado por el usuario y devuelve un diagnóstico.
    """
    try:
        logging.info(f"Mensaje recibido: {message.text}")
        response = chatbot.diagnose(message.text)
        logging.info(f"Respuesta generada: {response}")
        return {"response": response}
    except Exception as e:
        logging.error(f"Error al diagnosticar: {e}")
        raise HTTPException(status_code=500, detail="Ocurrió un error al procesar su solicitud.")
