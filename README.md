# 🏫 AulaOffline

Asistente educativo con IA para escuelas rurales de Latinoamérica.

## ¿Qué es?
AulaOffline usa Gemma 4 localmente (sin internet) para ayudar a maestros y alumnos de zonas rurales con acceso irregular a conectividad.

## Funcionalidades
- ❓ Responde preguntas adaptadas al grado del alumno
- 📝 Genera ejercicios por materia y tema
- 👩‍🏫 Asiste al maestro con planes de clase y actividades

## Tecnología
- Gemma 4 via Ollama (100% local, sin internet)
- FastAPI (Python)
- HTML/CSS/JS

## Instalación
1. Instalar Ollama: https://ollama.com
2. Bajar el modelo: `ollama pull gemma4`
3. Instalar dependencias: `pip install fastapi uvicorn requests`
4. Ejecutar: `uvicorn app:app --reload`
5. Abrir: http://localhost:8000
