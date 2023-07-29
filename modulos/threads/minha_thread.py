from time import sleep
from threading import Thread

class MinhaThread(Thread):
    def __init__(self, mensagem, tempo):
        self.mensagem = mensagem 
        self.tempo = tempo 

        super().__init__()
    
    def run(self):
        sleep(self.tempo)
        print(self.mensagem)

t1 = MinhaThread('Thread 1 ', 5)
t1.start()

t2 = MinhaThread('Thread 2 ', 8)
t2.start()

t3 = MinhaThread('Thread 3 ', 2)
t3.start()

for i in range(10):
    print(i)
    sleep(1)