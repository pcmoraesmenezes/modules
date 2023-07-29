import random 
# Funções:
# seed
#   -> Inicializa o gerador de random (por isso "números pseudoaleatórios")
# random.seed(0) #Extingue a aleatoriedade do código

# random.randrange(início, fim, passo)
#   -> Gera um número inteiro aleatório dentro de um intervalo específico
r_range = random.randrange(0, 100, 2) # Esse dois como parametro indica que vai pular de dois em dois ou seja para esse código será gerados apenas numeros pares
print(f'random.randrange -> {r_range}')

# random.randint(início, fim)
#   -> Gera um número inteiro aleatório dentro de um intervalo "sem passo"
r_int = random.randint(1000, 100000)
print(f'random.radint -> {r_int}')


# random.uniform(início, fim)
#   -> Gera um número flutuante aleatório dentro de um intervalo "sem passo"
r_float = random.uniform(0,10)
print(f'random.uniform -> {r_float}')

# random.shuffle(SequenciaMutável) -> Embaralha a lista original
lista = ['Acordar', 'Escovar os dentes', 'Fazer café', 'Estudar', 'Ler', 'Academia', 'Almoço']
random.shuffle(lista)
print(f'random.shuffle -> {lista}')

# random.sample(Iterável, k=N)
#   -> Escolhe elementos do iterável e retorna outro iterável (não repete)
nova_lista = random.sample(lista, k=3)
print(f'random.sample -> {nova_lista}')

# random.choices(Iterável, k=N)
#   -> Escolhe elementos do iterável e retorna outro iterável (repete valores)
lista_repetida = random.choices(lista, k=3)
print(f'random.choiceS -> {lista_repetida}')

# random.choice(Iterável) -> Escolhe um elemento do iterável
lista_unica = random.choice(lista)
print(f'random.choice -> {lista_unica}')