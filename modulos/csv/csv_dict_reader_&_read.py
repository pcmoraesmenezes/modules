from pathlib import Path
import csv

CAMINHO_CSV = Path(__file__).parent / 'ler.csv'

with open(CAMINHO_CSV, 'r', encoding='utf-8') as arquivo:
    leitor = csv.reader(arquivo)
    
    print("Lendo como lista:")
    for linha in leitor:
        #Para ler uma unica linha -> print(linha[x])
        print(linha)

# Reabrir o arquivo para usar o csv.DictReader
with open(CAMINHO_CSV, 'r', encoding='utf-8') as arquivo:
    ler_dicionario = csv.DictReader(arquivo)

    print("\nLendo como dicionário:")
    for linha_dict in ler_dicionario:
        print(linha_dict)
        # print(linha_dict['Nome'])
        # print(linha_dict['Idade'])
        # print(linha_dict['Profissão'])

