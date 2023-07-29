import calendar

# print(calendar.calendar(2022)) #Exibe o calendario inteiro do ano desejeado
# print(calendar.month(2023,7)) #Exibe o mes de um ano
print(calendar.monthrange(2023,7)) ##Retorna uma tupla com o dia da semana em formato numerico e o ultimo dia da semana
print(list(enumerate(calendar.day_name)))

numero_primeiro_dia, ultimo_dia = calendar.monthrange(2023,5)
print(calendar.day_name[numero_primeiro_dia])
print(calendar.day_name[calendar.weekday(2022,12,ultimo_dia)])

for week in calendar.monthcalendar(2023,5):
    print(list(enumerate(week)))
    for day in week:
        if day == 0:
            continue
        print(day)