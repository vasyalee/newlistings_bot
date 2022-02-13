import smtplib, ssl
from load_config import *

config = load_config('config.yml')

def send_notification(coin):
    port = 465 #For SSL
    smtp_server = 'smtp.gmail.com'
    sent_from = config['EMAIL_ADDRESS']
    to = [config['EMAIL_ADDRESS']]
    subject = f'Binance is going to list {coin} soon. Buy it now to sell in the future!'
    body = f'Check it out here https://www.binance.com/en/support/announcement/c-48 or find token info in Google https://www.google.com/search?q={coin}+token&oq={coin}+token&aqs=chrome..69i57.5748j0j1&sourceid=chrome&ie=UTF-8'
    message = 'Subject: {}\n\n{}'.format(subject, body)

    try:
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
            server.login(sent_from, config['EMAIL_PASSWORD'])
            server.sendmail(sent_from, to, message)
    except Exception as e:
        print(e)

