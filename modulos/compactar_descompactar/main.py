import os
import shutil
from pathlib import Path
from zipfile import ZipFile

CAMINHO_RAIZ = Path(__file__).parent #DIretorio pai, ou seja aonde o arquivo está
CAMINHO_ZIP_DIR = CAMINHO_RAIZ / 'main_zip' #Caminho para a pasta main_zip, uma subpasta do CAMINHO_RAIZ
CAMINHO_COMPACTADO = CAMINHO_RAIZ / 'main_compactado.zip' #Caminho para o arquivo zip
CAMINHO_DESCOMPACTADO = CAMINHO_RAIZ / 'main_descompactado' # Caminho para a pasta main_descompactado


#O código abaixo serve para remover os diretorios e os arquivos
shutil.rmtree(CAMINHO_ZIP_DIR, ignore_errors=True) #REmove o diretorio 'main_zip', o ignore_errors é para caso o diretorio não exista
Path.unlink(CAMINHO_COMPACTADO, missing_ok=True) #REmove o arquivo, ignorando caso ele não exista
shutil.rmtree(str(CAMINHO_COMPACTADO).replace('.zip', ''), ignore_errors=True) #REmove o diretorio e todo o seu conteudo. ESse trecho substitui a extensão .zip  do 
#arquivo para obter o nome da pasta pra ser removido
shutil.rmtree(CAMINHO_DESCOMPACTADO, ignore_errors=True) #REmove o diretorio

CAMINHO_ZIP_DIR.mkdir(exist_ok=True) #Cria um diretorio chamado 'main_zip'

def criar_arquivos(qtd: int, zip_dir:Path): #CRiando uma função, irá receber a quantidade de arquivos a ser criados e aonde os arquivos serão criados
    for i in range(qtd): #O i irá percorrer toda a quantidade dos arquivos
        texto = 'arquivo_%s' % i 
        #Nesta linha, estamos criando uma string chamada "texto" utilizando o operador de formatação % para inserir o valor da variável i no marcador de posição %s.
        # O resultado será uma string composta pela palavra "arquivo_" seguida pelo valor atual de i, que será usado posteriormente como o nome dos arquivos criados
        # na função criar_arquivos().
        with open(zip_dir / f'{texto}.txt', 'a') as arquivo: #O trecho zip_dir é o caminho até o arquivo o / é uma concatenação entre os caminhos, ele está concatenando
            #com o nome do arquivo que está sendo criado com a extensão .txt
            arquivo.write(texto)

criar_arquivos(10,CAMINHO_ZIP_DIR) #Criando dez arquivos no caminho CAMINHO_ZIP_DIR

with ZipFile(CAMINHO_COMPACTADO, 'w') as zip: #ZipFIle está fornecendo funcionalidades para ler, escrever e manipular arquivos no formato zip
    for root, dirs, files in os.walk(CAMINHO_ZIP_DIR): #os.walk é uma função recursiva que irá percorrer todo o diretorio, root é o diretorio atual, dirs são 
        #os subdiretorios e files são os arquivos
        for file in files:
            # print(file)
            zip.write(os.path.join(root, file), file) #os.path.join está unindo o os caminhos do diretorio root e o nome do arquivo, file representa o nome do 
            #caminho sem o arquivo. Zip.write está adicionando o arquivo ZIP 

with ZipFile(CAMINHO_COMPACTADO, 'r') as zip:
    for arquivo in zip.namelist():#compactando todos os arquivos em um unico arquivo zip
        print(arquivo)

with ZipFile(CAMINHO_COMPACTADO, 'r') as zip:
    zip.extractall(CAMINHO_DESCOMPACTADO)#descompactando todos os arquivos em um unico arquivo zip