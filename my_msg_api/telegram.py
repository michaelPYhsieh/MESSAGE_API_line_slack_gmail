# https://core.telegram.org/bots/api#sendmessage


def send_telegram(config, content=None, sendtype='text'):
    token = config['token']
    chat_id = config['chat_id']
    if sendtype.lower() in ('message', 'text'):
        url = f'https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={content}'
    elif sendtype.lower() in ('photo', 'pic', 'picture'):
        url = f'https://api.telegram.org/bot{token}/sendPhoto?chat_id={chat_id}&photo={content}'
    import requests
    response = requests.get(url)


if __name__ == "__main__":
    import toml
    CONFIG = toml.load('config.toml')['TELEGRAM']['bot_1']
    send_telegram(CONFIG, 'hi')
    send_telegram(CONFIG, 'https://telegram.org//img/t_logo.png',
                  sendtype='Photo')
