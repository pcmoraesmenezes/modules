from threading import Lock
from threading import Thread
from time import sleep

class Ingressos:
    def __init__(self, estoque: int) -> None:
        self.estoque = estoque
        self.lock = Lock()
    
    def comprar(self, quantidade):
        self.lock.acquire()
        if self.estoque < quantidade:
            print('Não temos estoque o suficiente! ')
            self.lock.release()
            return
        
        sleep(1)

        self.estoque -= quantidade
        print(f'Você comprou {quantidade} de ingresso(s), ainda resta(m) {self.estoque}')
        self.lock.release()

if __name__ == '__main__':
    ingressos = Ingressos(10)
    for i in range(1, 10):
        t = Thread(target= ingressos.comprar, args=(i,))
        t.start()
        print(ingressos.estoque)

"""
Vamos analisar o que está acontecendo:

A classe Ingressos possui um atributo estoque, que é a quantidade de ingressos disponíveis para venda.

No construtor __init__, é definido o Lock como self.lock, que será usado para proteger a seção crítica do código (a modificação do estoque).

O método comprar(self, quantidade) é usado para simular a compra de ingressos. Ele tenta adquirir o lock usando self.lock.acquire(). Se o estoque não tiver ingressos suficientes para a quantidade solicitada, ele imprime a mensagem "Não temos estoque o suficiente!" e libera o lock com self.lock.release().

Se houver estoque disponível para a quantidade solicitada, ele aguarda por 1 segundo (simulando o processo de compra) e, em seguida, deduz a quantidade comprada do estoque e imprime uma mensagem informando a quantidade comprada e o estoque restante.

No bloco if __name__ == '__main__':, você cria uma instância da classe Ingressos com 10 ingressos disponíveis.

Em seguida, você inicia 9 threads, cada uma tentando comprar uma quantidade de ingressos de 1 a 9 (usando o loop for i in range(1, 10)).

Antes de cada compra, você imprime o valor atual do estoque (mas não está sendo atualizado em tempo real).

Em seguida, as threads executam o método comprar(quantidade) para tentar comprar a quantidade de ingressos especificada. Como o estoque é de apenas 10 ingressos, algumas threads não poderão comprar o número solicitado (a partir da 4ª tentativa, não haverá estoque suficiente).

As mensagens "Você comprou X de ingresso(s), ainda resta(m) Y" são impressas quando há estoque suficiente. As mensagens "Não temos estoque o suficiente!" são impressas quando não há estoque suficiente.

Como resultado, algumas threads conseguem comprar ingressos, enquanto outras não podem devido à falta de estoque.
"""