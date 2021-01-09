import toml


from my_msg_api.slack import send_slack
from my_msg_api.line import send_line
from my_msg_api.gmail import send_gmail


CONFIG = toml.load('config.toml')['SLACK']['workspace_1']
send_slack(CONFIG, 'demo')


CONFIG = toml.load('config.toml')['LINE']['channel_1']
send_line(CONFIG, 'demo')


CONFIG = toml.load('config.toml')['GMAIL']['account_1']
send_gmail(CONFIG, recipient='', subject='demo',
           content='something', isHtml=False)
