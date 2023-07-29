import os
from dotenv import load_dotenv
import pathlib
from string import Template
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import smtplib

CAMINHO_ARQUIVO = pathlib.Path(__file__).parent / 'texto_para_email.html'

load_dotenv()

# Dados do remetente
remetente = os.getenv('FROM_EMAIL', '')
destinatario = os.getenv('DESTINATARIO', '')

# Configurações SMTP
smtp_server = "smtp.gmail.com"
smtp_port = 587
smtp_user = os.getenv('FROM_EMAIL', '')
smtp_password = os.getenv('EMAIL_PASSWORD', '')

with open(CAMINHO_ARQUIVO, 'r') as file:
    arquivo = file.read()
    template = Template(arquivo)
    texto = template.substitute(nome='Paulo')

mime_multipart = MIMEMultipart()
mime_multipart['From'] = remetente
mime_multipart['To'] = destinatario
mime_multipart['Subject'] = 'Este é o assunto do email'

# Corpo do email
corpo_email = MIMEText(texto, 'html', 'utf-8')
mime_multipart.attach(corpo_email)

# Anexar a imagem
caminho_imagem = pathlib.Path(__file__).parent / 'download.jpeg'
with open(caminho_imagem, 'rb') as image_file:
    imagem = MIMEImage(image_file.read())
    imagem.add_header('Content-Disposition', 'attachment', filename=str(caminho_imagem))
    mime_multipart.attach(imagem)

# Enviar o email
with smtplib.SMTP(smtp_server, smtp_port) as server:
    server.ehlo()
    server.starttls()
    server.login(smtp_user, smtp_password)
    server.send_message(mime_multipart)
    print('Email enviado com sucesso!')
