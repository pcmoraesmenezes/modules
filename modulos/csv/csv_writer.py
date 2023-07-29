import csv
from pathlib import Path

CAMINHO_CSV = Path(__file__).parent/'escrever.csv'

# Exemplo de lista de dicionários com informações de pessoas
lista_de_pessoas = [
    {
        'nome': 'João',
        'idade': 30,
        'profissao': 'Engenheiro'
    },
    {
        'nome': 'Maria',
        'idade': 25,
        'profissao': 'Médica'
    },
    {
        'nome': 'Pedro',
        'idade': 22,
        'profissao': 'Estudante'
    },
    {
        'nome': 'Laura',
        'idade': 28,
        'profissao': 'Advogada'
    },
    {
        'nome': 'Carlos',
        'idade': 35,
        'profissao': 'Arquiteto'
    },
    {
        'nome': 'Ana',
        'idade': 40,
        'profissao': 'Professor'
    },
    {
        'nome': 'Mariana',
        'idade': 27,
        'profissao': 'Jornalista'
    },
    {
        'nome': 'Rafael',
        'idade': 32,
        'profissao': 'Programador'
    },
    {
        'nome': 'Julia',
        'idade': 29,
        'profissao': 'Psicóloga'
    },
    {
        'nome': 'Fernanda',
        'idade': 38,
        'profissao': 'Advogada'
    }
]

with open(CAMINHO_CSV, 'w',encoding='utf-8') as file:
    colunas = lista_de_pessoas[0].keys()
    escritor = csv.writer(file)
    escritor.writerow(colunas)

    for pessoa in lista_de_pessoas:
        escritor.writerow(pessoa.values())

with open(CAMINHO_CSV, 'w', encoding='utf-8') as file:
    nome_colunas = lista_de_pessoas[0].keys()
    escritor = csv.DictWriter(file, fieldnames=nome_colunas)

    escritor.writeheader()

    for pessoa in lista_de_pessoas:
        escritor.writerow(pessoa)