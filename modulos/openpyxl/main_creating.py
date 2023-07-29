from pathlib import Path
from openpyxl import Workbook
from openpyxl.worksheet.worksheet import Worksheet
import subprocess

ROOT_FOLDER = Path(__file__).parent
ROOT_FILE = ROOT_FOLDER / 'arquivos'
WORKBOOK_PATH = ROOT_FILE / 'workbook.xlsx'
#  Nome para a planilha
SHEET_NAME = "spreadsheet"

workbook = Workbook()
#  Criamos a planilha
workbook.create_sheet(SHEET_NAME, 0)

#  Selecionou a planilha
worksheet: Worksheet = workbook[SHEET_NAME]  # type: ignore

#  Remover uma planilha

workbook.remove(workbook['Sheet'])

#  Criando cabeçalhos
worksheet.cell(1, 1, 'Name')
worksheet.cell(1, 2, 'Age')
worksheet.cell(1, 3, 'Score')


#       idade           idade       nota
students = [
    [
        'Paulo',         19,            10,
    ],
    [
        'Alberto',       18,             6,
    ],
    [
        'Joana',         18,             3,
    ],
    [
        'MCLOVIN',       18,            10,
    ],
]

subprocess.run('clear')
# Jeito dificil
# for i, student_row in enumerate(students, start=2):
#     print(f'Row: {i}, Content {student_row}\n')
#     for j, student_column in enumerate(student_row, start=1):
#         print(f'Column {j}, Content {student_column}')
#         print('-'*100)
#         worksheet.cell(i, j, student_column)

for student in students:
    worksheet.append(student)

workbook.save(WORKBOOK_PATH)
