push:
	git add .
	git commit -m "$(shell date '+%Y/%m/%d %A %H:%M:%S')"
	git push
	
pfreeze:
	pip freeze > requirements.txt
	
pipreq:
	pip install -r requirements.txt

noti01-slack:	
	@curl -X POST ${Webhook} \
	-H 'Content-Type: application/json' \
	-d '{"username": "noti01", "text": "hi"}'

ch1-line:
	@curl -X POST https://api.line.me/v2/bot/message/broadcast \
	-H 'Content-Type: application/json' \
	-H 'Authorization: Bearer ${CHANNEL_ACCESS_TOKEN}' \
	-d '{"messages":[{"type": "text", "text": "hi"}]}'

bot_1-telegram:
	@curl -X POST https://api.telegram.org/bot${token}/sendMessage \
	-H 'Content-Type: application/json' \
	-d '{"chat_id": ${chat_id}, "text": "hii"}'

bot_1-telegram-get:
	@curl -X GET https://api.telegram.org/bot${token}/sendMessage?chat_id=${chat_id}&text=hi
