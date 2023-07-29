# Exercício solucionado: calculando as datas e parcelas de um empréstimo
# Maria pegou um empréstimo de 1.000.000
# para realizar o pagamento em 5 anos.
# A data em que ela pegou o empréstimo foi
# 20/12/2020 e o vencimento de cada parcela
# é no dia 20 de cada mês.
# - Crie a data do empréstimo
# - Crie a data do final do empréstimo
# - Mostre todas as datas de vencimento e o valor de cada parcela

from datetime import datetime
from dateutil.relativedelta import relativedelta

valor_total = 1000000
num_parcelas = 60

# Cálculo do valor de cada parcela
valor_parcela = valor_total / num_parcelas

data_inicio = datetime(day=20, month=12, year=2020)
data_fim = data_inicio + relativedelta(years=5)  # Avança 5 anos a partir da data de início

i = 0
while data_inicio < data_fim:
    print(f'Data: {data_inicio.strftime("%d/%m/%Y")}, Valor da parcela: R${valor_parcela:.2f}')
    data_inicio = data_inicio + relativedelta(months=1)
    i += 1
