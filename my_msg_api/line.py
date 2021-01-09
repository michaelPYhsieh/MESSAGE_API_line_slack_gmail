import toml
CONFIG = toml.load('config.toml')['LINE']['channel_1']


def send_line(config, text=None):
    token = config['CHANNEL_ACCESS_TOKEN']
    url = "https://api.line.me/v2/bot/message/broadcast"  # broadcast
    headers = {'Content-Type': 'application/json'}
    headers['Authorization'] = f'Bearer {token}'
    data = {'messages': []}
    # data['messages'] += [{'type': 'text', 'text': '111'}]
    data['messages'] += [{'type': 'text', 'text': text}]
    import json
    data = json.dumps(data)
    import requests
    response = requests.request(
        method="POST", url=url, headers=headers, data=data)


if __name__ == '__main__':
    send_line(CONFIG, 'hi')
