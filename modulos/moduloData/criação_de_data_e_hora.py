from datetime import datetime
from pytz import timezone #biblioteca para pegar a 'timezone' - fuso horario dos lugares   


# data = datetime(2023, 7, 21, 6, 10)
# print(data)
data_str_data = '2023-7-21 06:10:22'
data_str_fmt = '%Y-%m-%d %H:%M:%S' #o formato e a data precisa ter o mesmo padrão

data = datetime.strptime(data_str_data, data_str_fmt)
print(data)

#Para conseguir a data exata agora do seu computador

data_agora = datetime.now()
print(data_agora)

#Bora ver quantas horas é agora em tokyo

data_em_tokyo = datetime.now(timezone('Asia/Tokyo'))
print(data_em_tokyo)

#Quer descobrir quantos segundos tem da sua data até o 01/01/1970?

hora_agora = datetime.now()
print(hora_agora.timestamp())

#Do timestamp até a sua data 
print(hora_agora.fromtimestamp(1689932057.715333))