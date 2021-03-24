import toml

from my_msg_api.slack import send_slack
from my_msg_api.line import send_line
from my_msg_api.gmail import send_gmail
from my_msg_api.telegram import send_telegram

if __name__ == '__main__':
    from pathlib import Path
    BASE_DIR = Path(__file__).resolve().parent
    CONF = toml.load(BASE_DIR/'config.toml')

    slack_ws1 = CONF['SLACK']['workspace_1']
    send_slack(slack_ws1, 'demo')

    line_ch1 = CONF['LINE']['channel_1']
    send_line(line_ch1, 'demo')

    gmail_ac1 = CONF['GMAIL']['account_1']
    send_gmail(gmail_ac1, recipient='', subject='demo',
               content='something', isHtml=False)

    tg_b1 = CONF['TELEGRAM']['bot_1']
    send_telegram(tg_b1, 'hi')
    send_telegram(tg_b1, 'https://telegram.org//img/t_logo.png',
                  sendtype='Photo')
