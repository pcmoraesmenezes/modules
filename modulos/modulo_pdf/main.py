from pathlib import Path
from PyPDF2 import PdfReader, PdfWriter, PdfMerger

PASTA_RAIZ = Path(__file__).parent
PASTA_PDF = PASTA_RAIZ / 'pasta_pdf'
PASTA_NOVA = PASTA_RAIZ / 'arquivos_novos'

RELATORIO = PASTA_PDF / 'R20230210.pdf'

PASTA_NOVA.mkdir(exist_ok=True)

reader = PdfReader(RELATORIO)

print(len(reader.pages))  # exibe o tamanho do pdf

# for page in reader.pages:
# a pagina é um iteravel, logo é possivel percorrer  ela
#  print(page)
#  print('-' *100)

page0 = reader.pages[0]
imagem0 = page0.images[0]

print(page0.extract_text())  # Exibe o texto da primeira pagina

with open(PASTA_NOVA / imagem0.name, 'wb') as fp:
    fp.write(imagem0.data)

for i, page in enumerate(reader.pages):  # para pegar o arquivo e replicar
    writer = PdfWriter()
    with open(PASTA_NOVA / f'pagina {i}.pdf', 'wb') as fp:
        writer.add_page(page)
        writer.write(fp)

files = [
    PASTA_NOVA / 'pagina 1.pdf',
    PASTA_NOVA / 'pagina 0.pdf',

]

merger = PdfMerger()
for file in files:
    merger.append(file)  # type: ignore

merger.write(PASTA_NOVA / 'MERGED.pdf')  # type: ignore
merger.close()
