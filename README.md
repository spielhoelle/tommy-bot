# Tommy-Bot
## Simple telegram chatbot trained on telegram/whatsapp chat export data

Proof of concept implementing a simple chatbot with python.

## Tech
- tensorflow rnn
- flask
- telegram-api
- interval/cron-job poll for new messages

## Get it up and running
1. Create a `.env` file with this structure:
	```
	FLASK_APP=app.py
	TELEGRAM_BOT_ID=bot1111111111:XXXXXXXXX-XXXXXXXXXXXXXXXXXXXXXXXXX
	```
2. Create a bot by chatting with the [Botfather](https://t.me/botfather). You will receive a token which comes in the newly by you created `.env` file from step 1.
3. Run it with `flask run` or `docker-compose up`
4. Send `yes` to the chatbot and it will react with `YEAAAHH`, send `no` and you get a `NOOOO` back.
