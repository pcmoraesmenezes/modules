import calendar
import locale

locale.setlocale(locale.LC_ALL, 'pt_br')
print(locale.getlocale())
print(calendar.calendar(2023))