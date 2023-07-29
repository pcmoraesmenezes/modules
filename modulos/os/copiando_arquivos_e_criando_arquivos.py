import os, shutil

HOME = os.path.expanduser('~')
print(HOME)

AREA_DE_TRABALHO = os.path.join(HOME, 'Área de Trabalho')
print(AREA_DE_TRABALHO  )

print(os.path.exists(AREA_DE_TRABALHO))

NOVA_PASTA = os.path.join(AREA_DE_TRABALHO, 'teste')
os.makedirs(NOVA_PASTA, exist_ok=True)