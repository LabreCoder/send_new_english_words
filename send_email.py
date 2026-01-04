import os
import smtplib
import email.message
from dotenv import load_dotenv
from get import get_last_id
from insert import insert_new_word

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
        print(type(id))
        int_id = int(id) + 1
        print(f'✅ Banco OK — ID retornado: {int_id}')
    except Exception as e:
        print('❌ ERRO no banco:', e)
        return

    # Dados do e-mail
    sender_email = 'jvlabremachado@gmail.com'
    receiver_email = 'jvlabremachado@id.uff.br'
    subject = f'Palavras novas em inglês para você aprender - Dia {int_id}'

    word = 'Awesome'
    body = f'''
        Olá, estamos aprendendo a palavra id: {int_id}# !!
        
        Aqui está a nova palavra do dia: {word} 🥳🥳🥳

        Ela significa "incrível", "fantástico" ou "impressionante".

        Exemplo de uso:

                That movie was awesome! I loved it.
                Tradução: Aquele filme foi incrível! Eu adorei.
        
        Continue aprendendo e se divertindo! 🚀📚
        '''

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
        insert_new_word(word, 'teste de frase')

    except smtplib.SMTPAuthenticationError:
        print('❌ Falha de autenticação: verifique App Password do Gmail')


if __name__ == "__main__":
    main()
