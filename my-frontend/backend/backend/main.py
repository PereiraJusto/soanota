from fastapi import FastAPI

#Criação da aplicação FastAPI
app = FastAPI()

#Cria  uma rota  na raiz ("/")  que responde  a requisições GET
@app.get("/")
def read_root():
    return {"message":"Hello, World!"}

# Nova rota que recebe  um parâmetro na URL
@app.get("/hello/{name}")
def say_hello(name:str):
    return {"message": f"Olá, {name}!"}