from pathlib import Path
import string
import locale
from datetime import datetime
import json

CAMINHO_ARQUIVO = Path(__file__).parent / 'recomendação.txt'

locale.setlocale(locale.LC_ALL, '')

def converte_para_brl(numero: float) -> str:
    brl = 'R$ '+ locale.currency(numero, symbol=False, grouping=True)
    return brl

data = datetime.now()
dados = dict(
    nome= 'Paulo César',
    data = data.strftime('%d/%m/%Y'),
    empresa = 'Monstros SA',
    telefone = '+55 (69) 8180-7723',
    salario = converte_para_brl(456_343_123)
)

# print(json.dumps(dados, indent=2, ensure_ascii=False))

texto = """
Prezado(a) $nome,

Informamos que lhe foi avaliado a carta de recomendação para a sua entrada ao time e ficamos muito satisfeitos com o seu desempenho. A data de ínicio é de $data. Gostariamos
que você entrasse em contato o mais rápido possível através deste numero: $telefone, o salário será de ${salario}, entretanto pode-se ser 
discutido.

Atenciosamente, ${empresa}.

Abraços $nome.
"""
template = string.Template(texto)
# print(template.substitute(dados))
# print(template.safe_substitute(dados)) #Garante que o texto será executado mesmo se ocorrer erro 

with open(CAMINHO_ARQUIVO, 'r') as file:
    #Garante que consigo trabalhar diretamente com o arquivo
    texto = file.read()
    template = string.Template(texto)
    print(template.substitute(dados))