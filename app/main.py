from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
# from . import models
# from .database import engine
from .routers import post, user,auth, vote

#13:34 horas

#Comentar bloque de codigo CTRL + K, CTRL + C
#Descomentar ctrl + k , ctrl + u

#Esta linea crea las tablas definidas en models 
#models.Base.metadata.create_all(bind=engine)

app = FastAPI()

"""
CORS
s un mecanismo de seguridad que controla quién puede acceder 
a tu API desde otro dominio diferente al que la sirve.

fetch('http://localhost:8000/').then(res=> res.json()).then(console.log)
"""
origins = ["*"]

app.add_middleware(
     CORSMiddleware,
     allow_origins=origins,
     allow_credentials=True,
     allow_methods=["*"],
     allow_headers=["*"],
)

app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(vote.router)

@app.get("/")
async def root():
     return {"message": "Hello World"}





