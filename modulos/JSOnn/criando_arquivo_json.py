import json
import os 

NOME_ARQUIVO = 'CRIA_JSON.json'
CAMINHO_ABSOLUTO = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__),
        NOME_ARQUIVO
    )
)

filme = {
    'title': 'O Senhor dos Anéis: A Sociedade do Anel',
    'original_title': 'The Lord of the Rings: The Fellowship of the Ring',

    'is_movie': True,
    'imdb_rating': 8.8,
    'year': 2001,
    'characters': ['Frodo', 'Sam', 'Gandalf', 'Legolas', 'Boromir'],
    'budget': None
}

with open(CAMINHO_ABSOLUTO, 'w', encoding='utf-8') as file:
    json.dump(filme, file, ensure_ascii=False, indent= 2)

with open(CAMINHO_ABSOLUTO, 'r', encoding='utf-8') as file:
    ler_arquivo = json.load(file)
    print(ler_arquivo)

