import qrcode
from PIL import Image
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from datetime import datetime
import pytz
import os

# Configuração do servidor SMTP
SMTP_SERVER = 'smtp.gmail.com'  # Servidor do seu e-mail
SMTP_PORT = 587
EMAIL_ADDRESS = 'rafaelquintinoamz@gmail.com'  # Seu e-mail
EMAIL_PASSWORD = 'rnqb igot vqpm xzsy'  # Senha do e-mail

def format_user_data(name, phone, email):
    return f"Nome: {name}\nNúmero de telefone: {phone}\nE-mail: {email}"

def display_qr_code(filename):
    image = Image.open(filename)
    image.show()

def send_email(recipient_email, subject, body, background_image_path):
    msg = MIMEMultipart('related')
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = recipient_email
    msg['Subject'] = subject

    # Cria o corpo do e-mail em HTML com a imagem de fundo
    html_body = f"""
    <html>
    <body style="background-image: url('cid:bg_image'); background-size: cover; font-family: Arial, sans-serif; color: white;">
        <div style="padding: 20px;">
            <h2>Comprovação de Inscrição</h2>
            <p>{body}</p>
        </div>
    </body>
    </html>
    """

    # Anexa o conteúdo HTML
    msg.attach(MIMEText(html_body, 'html'))

    # Abre e anexa a imagem de plano de fundo
    with open(background_image_path, 'rb') as img_file:
        img = MIMEImage(img_file.read())
        img.add_header('Content-ID', '<bg_image>')
        img.add_header('Content-Disposition', 'inline', filename=os.path.basename(background_image_path))
        msg.attach(img)

    try:
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            server.sendmail(EMAIL_ADDRESS, recipient_email, msg.as_string())
        print(f"E-mail enviado para {recipient_email} com sucesso!")
    except Exception as e:
        print(f"Erro ao enviar e-mail: {e}")

def main():
    print("Cadastro de Usuário")
    name = input("Digite o nome: ")
    phone = input("Digite o número de telefone: ")
    email = input("Digite o e-mail: ")

    # Formata os dados do usuário
    user_data = format_user_data(name, phone, email)

    # Obtém a data e hora da inscrição
    timezone = pytz.timezone('America/Sao_Paulo')
    registration_time = datetime.now(timezone).strftime('%d/%m/%Y %H:%M:%S')

    # Formata o corpo do e-mail
    email_body = f"""
    Nome: {name}
    Número de telefone: {phone}
    E-mail: {email}
    Data e hora de inscrição: {registration_time}
    """

    # Caminho para a imagem de fundo
    background_image_path = 'C:/Users/55889/Desktop/Envio email Python/oculos.jpg'  # Altere para o caminho da sua imagem

    # Envia o e-mail de comprovação com plano de fundo
    send_email(email, 'Comprovação de Inscrição', email_body, background_image_path)

    print("\nCadastro realizado com sucesso!")
    print("O e-mail de comprovação com plano de fundo foi enviado.")
    print("\nDados do usuário:")
    print(user_data)

if __name__ == "__main__":
    main()
