from  argparse import ArgumentParser

parser = ArgumentParser()

parser.add_argument(
    '-b', '--basic',
    help='Mostra "Olá mundo" Na tela ',
    #type = str, #define o tipo
    metavar= 'STRING',
    #default="Olá mundo! ", #valor padrão
    required = False, #torna o uso obrigatorio ou nao de argumentos 
    #nargs='+' #cria uma lista 
    action = 'append', #recebe o argumento mais de uma vez
)

args = parser.parse_args()

if args.basic is None:
    print('Você não passou o valor de B')
    print(args.basic)
else:
    print(f"O valor de B é {args.basic}")