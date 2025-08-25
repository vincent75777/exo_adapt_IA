from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
import psycopg2
import geojson

# Initialisation de l'application FastAPI
app = FastAPI()

# Autoriser toutes les origines (CORS) — pour développement local
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # En production, restreindre cette liste !
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
