import subprocess
import sys

plataforma = sys.platform

print('-'*182)
print(sys.platform) # Exibe o sistema operacional que você está utilizando
# Lógica para fazer esse programa funcionar em todos os sistemas operacionais
if plataforma in ['linux', 'linux2', 'darwin']:
    subprocess.run('clear', shell=True)

    cmd = ['ping', '127.0.0.1', '   -c', '4']
    listar = ['ls', '-lah', '/']
    escrever = f'echo "ABACATE" > TESTE'
    ler = ['cat', 'TESTE']

    processo = subprocess.run(
        cmd, capture_output=True,
        text=True, # Exibe a saída em formato de texto, se utilizado deve remover o decode para evitar erros
        # encoding= 'cp850' # Enconding deve ser utilizado no Windows para evitar erro nos caracteres
    )

    processo2 = subprocess.run(
        listar, capture_output=True,
        text=True
    )
    
    # Create and write to the file 'TESTE'
    subprocess.run(escrever, shell=True)

    processo4 = subprocess.run(
        ler, capture_output=True,
        text=True
    )
    
    print('-'*182)

    print(processo.args) # Retorna os argumentos passados -> a lista com os comandos

    print('-'*182)

    print(processo.stderr) #exibe a saída em caso de erro, caso não tenha erro, a saída e vazia

    print('-'*182)

    # print(processo.stdout.decode('utf_8')) # Utilizando a função .decode ele exibe a saída em formato de texto, note que sem ele a saída é em formato de bytes
    print(processo.stdout) # Note que com o text true não é preciso utilizar o decode para exibir a saída em formato de texto
    print('-'*182)

    print(processo.returncode) #retorna 0 se o código foi executado com sucesso

    print('-'*182)

    print(processo2.stdout)

    print('-'*182)

    print(processo4.stdout)

    print('-'*182)

else:
    cmd = ['ping', '127.0.0.1']
    subprocess.run('cls', shell=True)

    processo = subprocess.run(
        cmd, capture_output=True,
        text=True, # Exibe a saída em formato de texto, se utilizado deve remover o decode para evitar erros
        encoding='cp850' # Enconding deve ser utilizado no Windows para evitar erro nos caracteres
    )

    print('-'*182)

    print(processo.args) # Retorna os argumentos passados -> a lista com os comandos

    print('-'*182)

    print(processo.stderr)

    print('-'*182)

    # print(processo.stdout.decode('utf_8')) # Utilizando a função .decode ele exibe a saída em formato de texto, note que sem ele a saída é em formato de bytes
    print(processo.stdout) # Note que com o text true não é preciso utilizar o decode para exibir a saída em formato de texto
    print('-'*182)

    print(processo.returncode)

    print('-'*182)
