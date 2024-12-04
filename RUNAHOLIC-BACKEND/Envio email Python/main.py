import qrcode
from PIL import Image
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime
import pytz

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

def send_email(recipient_email, subject, body):
    msg = MIMEMultipart()
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = recipient_email
    msg['Subject'] = subject

    # Corpo do e-mail
    msg.attach(MIMEText(body, 'plain'))

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
    Comprovação de Inscrição

    Nome: {name}
    Número de telefone: {phone}
    E-mail: {email}
    Data e hora de inscrição: {registration_time}
    """

    # Envia o e-mail de comprovação
    send_email(email, 'Comprovação de Inscrição', email_body)

    print("\nCadastro realizado com sucesso!")
    print("Os dados foram salvos no QR Code e o e-mail de comprovação foi enviado.")
    print("\nDados do usuário:")
    print(user_data)

if __name__ == "__main__":
    main()

# def generate_qr_code(data, filename='user_qrcode.png'):
#     qr = qrcode.make(data)
#     qr.save(filename)
#     print(f"QR Code salvo como {filename}")
#     return filename

    # Gera o QR Code e salva em um arquivo
    # qr_code_file = generate_qr_code(user_data)

    # Exibe o QR Code na tela
    # display_qr_code(qr_code_file)
