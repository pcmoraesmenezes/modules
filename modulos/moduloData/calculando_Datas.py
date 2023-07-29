from datetime import datetime
from dateutil.relativedelta import relativedelta

fmt = '%d/%m/%Y %H:%M:%S'
data_inicio = datetime.strptime('18/05/1964 9:45:35', fmt)
data_fim = datetime.strptime('05/06/2004 6:43:17', fmt )

delta = data_fim - data_inicio
print(delta.total_seconds())

print(data_fim)
print(data_fim + relativedelta(minutes=10, seconds=20, hours=4, years=2, months= 5, days=5, ))
