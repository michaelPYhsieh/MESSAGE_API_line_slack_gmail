import toml
CONFIG = toml.load('config.toml')['GMAIL']['account_1']


def send_gmail(config, recipient=None, subject=None, content=None, isHtml=False):
    gmail_user = config['GMAIL_USER']
    gmail_password = config['GMAIL_PASSWORD']
    gmail = {'host': 'smtp.gmail.com',
             'port': 465,
             'user': gmail_user,
             'password': gmail_password}
    import smtplib
    conn_gmail = smtplib.SMTP_SSL(gmail['host'], gmail['port'])
    conn_gmail.login(gmail['user'], gmail['password'])
    import email.message
    msg = email.message.EmailMessage()
    msg['From'] = gmail_user
    msg['To'] = recipient or gmail_user
    msg['Subject'] = subject  # opt
    if isHtml:
        msg.add_alternative(content, subtype='html')  # html信件
    else:
        msg.set_content(content)  # 純文字信件
    conn_gmail.send_message(msg)
    conn_gmail.close()


if __name__ == '__main__':
    subject = '主旨'
    content = '<h3>測試一</h3>測試二'
    send_gmail(CONFIG, recipient='', subject=subject,
               content=content, isHtml=True)
