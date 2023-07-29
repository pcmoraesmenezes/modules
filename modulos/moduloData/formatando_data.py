from datetime import datetime

data = datetime.strptime('2023-07-21 07:01:43', '%Y-%m-%d %H:%M:%S')
print(data)

print(data.strftime('%d/%m/%Y'))
print(data.strftime('%d/%m/%Y %H:%M'))
print(data.strftime('%d/%m/%Y %H:%M:%S'))

print(data.strftime('%Y'), data.year)
print(data.strftime('%m'), data.month)
print(data.strftime('%d'), data.day)
print(data.strftime('%H'), data.hour)
print(data.strftime('%M'), data.minute)
print(data.strftime('%S'), data.second)

#O valor formatado é retornado em string, mas acessando diretamente obtemos valores inteiros
