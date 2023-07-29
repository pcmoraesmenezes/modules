from time import sleep
from threading import Thread

class ContadorThread(Thread):
    def run(self):
        for i in range(1, 6):
            print(f"Contagem: {i}")
            sleep(1)

# Criando a instância da thread
thread = ContadorThread()

# Iniciando a thread chamando o método start()
thread.start()

# Executando uma ação no thread principal
for _ in range(3):
    print("Ação no thread principal")
    sleep(2)

# Aguardando a thread terminar com o método join()
thread.join()

print("Fim do programa")
