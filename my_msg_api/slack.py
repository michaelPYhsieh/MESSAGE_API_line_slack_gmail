import toml
CONFIG = toml.load('config.toml')['SLACK']['workspace_1']


# app: slack.com/apps/A0F7XDUAZ-incoming-webhooks


def send_slack(config, text=None, username=None, icon_emoji=None):
    url = config['Webhook']
    headers = {'Content-Type': 'application/json'}
    data = {}
    data['username'] = username or 'noti01'
    data['icon_emoji'] = icon_emoji or ':ghost:'
    data['text'] = text or 'hiiiii'
    import json
    data = json.dumps(data)
    import requests
    response = requests.request(
        method="POST", url=url, headers=headers, data=data)


if __name__ == "__main__":
    send_slack(CONFIG, 'hi')
