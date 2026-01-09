import os
import smtplib
import email.message
from dotenv import load_dotenv
from get import get_last_id
from insert import insert_new_word
from get_word import get_random_word
from get_phrase import get_definition

def main():
    print('🔹 Iniciando teste...')

    # Carrega o .env
    load_dotenv()

    # Teste 1 — .env
    sender_password = os.getenv('EMAIL_PASSWORD')
    if not sender_password:
        print('❌ ERRO: EMAIL_PASSWORD não carregada do .env')
        return
    print('✅ .env carregado')

    # Teste 2 — Banco
    try:
        id = get_last_id()
        int_id = int(id) + 1
        print(f'✅ Banco OK — ID retornado: {int_id}')
    except Exception as e:
        print('❌ ERRO no banco:', e)
        return

    # Dados do e-mail
    sender_email = 'jvlabremachado@gmail.com'
    receiver_email = 'jvlabremachado@id.uff.br'
    subject = f'Palavras novas em inglês para você aprender - Dia {int_id}'

    word = get_random_word()
    results = get_definition(word)
    definitions_text = ""
    examples_text = ""

    for i, (definition, example) in enumerate(results, start=1):
        if i != 1:
            definitions_text += f"                      Definition {i}: {definition}\n"
            examples_text += f"                      Example {i}: {example}\n"
        else:
            definitions_text += f"          Definition {i}: {definition}\n"
            examples_text += f"          Example {i}: {example}\n"

    body = f"""
        Hello, we are learning word ID: {int_id}#!!

        Here is the new word of the day: {word} 🥳🥳🥳

        It means:

            {definitions_text}

        Examples of usage:

            {examples_text}

        Keep learning and have fun! 🚀📚
    """
    for i in range(len(results)):
        j = 0
        insert_new_word(word, results[i][j], results[i][j + 1])

    # Teste 3 — SMTP + envio
    
    try:
        msg = email.message.EmailMessage()
        msg['From'] = sender_email
        msg['To'] = receiver_email
        msg['Subject'] = subject
        msg.set_content(body)

        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(sender_email, sender_password)
            print('✅ Login no Gmail OK')
            smtp.send_message(msg)

        print('📧 E-mail enviado com sucesso!')
        
    except smtplib.SMTPAuthenticationError:
        print('❌ Falha de autenticação: verifique App Password do Gmail')


if __name__ == "__main__":
    main()
