#  Ler/Alterar dados de uma planilha
from pathlib import Path
from openpyxl import Workbook, load_workbook
from openpyxl.worksheet.worksheet import Worksheet


ROOT_FOLDER = Path(__file__).parent
ROOT_FILE = ROOT_FOLDER / 'arquivos'
WORKBOOK_PATH = ROOT_FILE / 'workbook.xlsx'
#  Nome para a planilha
SHEET_NAME = "spreadsheet"

#  Carregando um arquivo do excel
workbook: Workbook = load_workbook(WORKBOOK_PATH)


#  Selecionou a planilha
worksheet: Worksheet = workbook[SHEET_NAME]  # type: ignore

for row in worksheet.iter_rows(min_row=2):
    for column in row:
        print(column.value, end='\t')
        if column.value == 'Paulo':
            worksheet.cell(column.row, 2, 20)  # type: ignore
    print()

#  É Possivel pegar valores especificos como se fosse planilhas do excel, ele
#  INforma o numero e a letra, basta pegar esses valores e usar um .value que
#  Obteremos o valor

print(worksheet['B3'].value)

#  Para alterar um valor:
worksheet['B3'].value = 14

#  Para adicionar novos valores
nova_linha = ['Andre', 23, 0]
linha_existe = False

for row in worksheet.iter_rows(values_only=True):
    if row == tuple(nova_linha):
        linha_existe = True
        break

if not linha_existe:
    worksheet.append(nova_linha)
workbook.save(WORKBOOK_PATH)
