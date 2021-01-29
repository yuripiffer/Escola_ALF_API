#MAIN - CODIGO_ESCOLA_ALF
import json
from fastapi import FastAPI

from Escola_Alf_Codigo_Logica import PROVA, ALUNO, criar_prova, info_prova, info_total_provas, preencher_quest_prova, criar_aluno 
from Escola_Alf_Codigo_Logica import info_aluno, info_total_alunos, criar_prova_aluno, preencher_prova_aluno, info_prova_aluno, info_notas_aluno 
from Escola_Alf_Codigo_Logica import provas_completas, aprovados, deletar_prova_aluno, deletar_aluno, deletar_prova

app = FastAPI()

## API GET que retorna informações de uma prova cadastrada
@app.get("/{idPROVA}")
async def create(idPROVA: str):
    return info_prova(idPROVA)

## API GET que retorna todas as provas cadastradas
@app.get("/PROVAS")
async def create():
    return info_total_provas()

## Criação de provas
@app.post("/{idPROVA}")
async def create(idPROVA: str, titulo: str, n_questões: int):
    return criar_prova(idPROVA, titulo, n_questões)

## Postagem de pergunta para prova já criada
@app.post("/idPROVA/{questao}")
async def create(idPROVA: str, q: int, resposta: str, peso: int):
    return preencher_quest_prova(idPROVA, q, resposta, peso)

## API GET que retorna informações de um aluno(a) cadastrado(a)
@app.get("/{idALUNO}")
async def create(idALUNO: str):
    return info_aluno(idALUNO)

## API GET que retorna todos os alunos(as) cadastrados(as)
@app.get("/ALUNOS")
async def create():
    return info_total_alunos()

## Postagem de aluno novo
@app.post("/{idALUNO}")
async def create(idALUNO: str, nome: str):
    return criar_aluno(idALUNO, nome)

## API GET que retorna informações de da prova já cadastrada para um aluno(a)
@app.get("/idALUNO/{idPROVA}")
async def create(idALUNO: str, idPROVA: str):
    return info_prova_aluno(idALUNO, idPROVA)

## Postagem de prova para aluno
@app.post("/idALUNO/{idPROVA}")
async def create(idALUNO: str, idPROVA: str):
    return criar_prova_aluno(idALUNO, idPROVA)

## Preencher uma questão de uma prova e aluno(a) já cadastrados
@app.post("/idALUNO/idPROVA/{questao}")
async def create(idALUNO: str, idPROVA: str, q: int, resposta: str):
    return preencher_prova_aluno(idALUNO, idPROVA, q, resposta)

## API GET lista de provas completas
@app.get("/PROVAS")
async def create():
    return provas_completas()

## API GET que retorna as notas computáveis de um aluno(a)
@app.get("/BOLETIM/{idALUNO}")
async def create(idALUNO: str):
    return info_notas_aluno(idALUNO)

## API GET que retorna a lista de aprovados
@app.get("/APROVADOS")
async def create():
    return aprovados()

## API DELETE que exclui prova do cadastro de aluno(a)
@app.delete("/idALUNO/{idPROVA}")
async def create(idALUNO:str, idPROVA:str):
    return deletar_prova_aluno(idALUNO, idPROVA)

## API DELETE que exclui aluno(a)
@app.delete("/{idALUNO}")
async def create(idALUNO:str):
    return deletar_aluno(idALUNO)

## API DELETE que exclui prova
@app.delete("/{idPROVA}")
async def create(idPROVA:str):
    return deletar_prova(idPROVA)
0

## 