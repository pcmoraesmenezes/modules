import os
from dotenv import load_dotenv

#Se o nome do seu arquivo .env for apenas .env apenas dar o load_dotenv() já é o suficiente, passar o caminho so é necessário em caso de nomes no arquivo

env_file_path = '/home/paulo/Desktop/vscode/udemy/modulo 6/modules/variaveis de ambiente/user_info.env'
if not os.path.isfile(env_file_path):
    print(f"O arquivo '{env_file_path}' não foi encontrado.")
else:
    load_dotenv(dotenv_path=env_file_path)
    bd_user = os.getenv('BD_USER')
    password = os.getenv('BD_PASSWORD')
    bd_port = os.getenv('BD_PORT')
    bd_host = os.getenv('BD_HOST')

    print(bd_user)
    print(password)
    print(bd_port)
    print(bd_host)

# print(os.environ) #os.environ mostra todos as variaveis de ambiente
print(os.getenv('BD_USER'))