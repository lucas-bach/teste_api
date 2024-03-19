from fastapi import FastAPI

app = FastAPI()

vendas = {
    1:{"Item": "lata",'Preco-unitario': 4, "quantidade": 5},
    2:{"Item": "garrafa 2L",'Preco-unitario': 15, "quantidade": 5},
    3:{"Item": "garrafa 750ml",'Preco-unitario': 10, "quantidade": 5},
    4:{"Item": "lata mini",'Preco-unitario': 2, "quantidade": 5},
}

@app.get("/")
def home():
    return {"Vendas": len(vendas)}


@app.get("/vendas/{id_venda}")
def pegar_venda(id_venda:int):
    if id_venda in vendas:
       return vendas[id_venda]
    else:
       return{"Erro": "ID Venda inesixtente"}