import toml


from my_msg_api.slack import send_slack
from my_msg_api.line import send_line
from my_msg_api.gmail import send_gmail
from my_msg_api.telegram import send_telegram


CONFIG = toml.load('config.toml')['SLACK']['workspace_1']
send_slack(CONFIG, 'demo')


CONFIG = toml.load('config.toml')['LINE']['channel_1']
send_line(CONFIG, 'demo')


CONFIG = toml.load('config.toml')['GMAIL']['account_1']
send_gmail(CONFIG, recipient='', subject='demo',
           content='something', isHtml=False)


CONFIG = toml.load('config.toml')['TELEGRAM']['bot_1']
send_telegram(CONFIG, 'hi')
send_telegram(CONFIG, 'https://telegram.org//img/t_logo.png',
              sendtype='Photo')
