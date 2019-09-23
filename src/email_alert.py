import smtplib, ssl

context = ssl.create_default_context()


def send_alert(config, message):
    with smtplib.SMTP_SSL(config['smtp_server'], config['SMTP_SSL_port'], context=context) as server:
        server.login(config['smtp_user'], config['smtp_password'])
        server.sendmail(config['smtp_user'], config['alert_recipient'], message)
