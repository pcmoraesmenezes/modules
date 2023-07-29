from time import sleep
from threading import Thread

def vai_demorar(mensagem, tempo):
    sleep(tempo)
    print(mensagem)

t1 = Thread(target=vai_demorar, args=('Olá mundo!! ', 10))
t1.start()
t1.join() #Impede a execução enquanto a thread não for executada 
print('Thread acabou!') #

# while t1.is_alive():
#     print('Esperando a thread.') bloqueia o codigo enquanto a thread ainda estiver viva
#     sleep(1)

