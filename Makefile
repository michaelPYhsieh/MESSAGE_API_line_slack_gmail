push:
	git add .
	git commit -m "$(shell date '+%Y/%m/%d %A %H:%M:%S')"
	git push
	
pfreeze:
	pip freeze > requirements.txt
	
pipreq:
	pip install -r requirements.txt
		
noti01-slack:	
	@curl -X POST --data-urlencode \
	"payload={\"username\": \"noti01\", \"text\": \"n01\", \"icon_emoji\": \":ghost:\"}" \
	${Webhook}

ch1-line:
	@curl -X POST https://api.line.me/v2/bot/message/broadcast \
	-H 'Content-Type: application/json' \
	-H 'Authorization: Bearer ${CHANNEL_ACCESS_TOKEN}' \
	-d '{"messages":[{"type": "text", "text": "hi"}]}'
