import os

senha = os.getenv('SENHA')

if senha is not None:
    print("Senha encontrada:", senha)
else:
    print("A variável de ambiente 'SENHA' não foi definida.")

#é possível criar uma variavel de ambiente pelo proprio vscode, assim torna desnecessário de certo modo o uso do arquivo .env