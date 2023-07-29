import os

CAMINHO = os.path.join('Área de Trabalho', 'vscode', 'python', 'udemy',
                       'modulo 6', 'arquivo.txt')
print(CAMINHO)

diretorio, arquivo = os.path.split(CAMINHO)
nome_arquivo, extensao_arquivo = os.path.splitext(arquivo)

print(nome_arquivo, extensao_arquivo)
print(os.path.exists('C:/Users/pczin/AppData/Local/Programs/Python/Python311/ \
                     python.exe'))
print(os.path.abspath('.'))
