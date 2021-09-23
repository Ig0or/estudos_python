from string import Template
from datetime import datetime
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import smtplib

# puxando template do html
with open('template.html', 'r') as html:
    template = Template(html.read())
    data_atual = datetime.now().strftime('%d/%m/%Y')
    corpo_msg = template.substitute(nome='Igor', data=data_atual)

# configura nome, destinatario e assunto
msg = MIMEMultipart()
msg['from'] = 'Pessoa 1'
msg['to'] = 'email@teste.com'
msg['subject'] = 'Assunto do E-mail'

corpo = MIMEText(corpo_msg, 'html')
msg.attach(corpo)

# anexa img
with open('imagem.jpg', 'rb') as img:
    img = MIMEImage(img.read())
    msg.attach(img)

# envia email
with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('email@teste.com', 'senhadoemailteste')
    smtp.send_message(msg)
    print('Email enviado com sucesso.')
