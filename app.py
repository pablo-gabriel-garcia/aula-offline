from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pydantic import BaseModel
import requests

app = FastAPI()

class Pregunta(BaseModel):
    texto: str
    grado: str = "4to grado"

@app.post("/preguntar")
def preguntar(p: Pregunta):
    prompt = f"""Eres AulaOffline, un asistente educativo para escuelas rurales de Latinoamérica.
Responde SIEMPRE en español, de forma clara y simple.
El alumno es de {p.grado}.
Pregunta: {p.texto}"""
    
    response = requests.post("http://localhost:11434/api/generate", json={
        "model": "gemma4",
        "prompt": prompt,
        "stream": False
    })
    return {"respuesta": response.json()["response"]}

@app.get("/")
def inicio():
    return FileResponse("index.html")
