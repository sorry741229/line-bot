from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

app = Flask(__name__)

line_bot_api = LineBotApi('Kfb2NVs7ZO9bCj3mKA1f7lFbl81eQ9tn5ZMxEh/dP1ot36GwHJik00ktxmrYRFU1oABlvL0Z4jLyrMPmlsVwPUkjEuHW2y8hjMyyFfNj4TwAT+UxhLC/GZu1qQKpWV7T73SyYFKqN7mLQ8BR0tcKtQdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('2e2e20dc3a4c33c48cad1411e0eb9d51')


@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    msg = event.message.text
    r = '我還沒那麼猛，不要再問了'
    if msg in ['hi', 'HI']:
        r = 'Hi'
    elif '飯了嗎' in msg :
        r = '我每天都很飽'
    elif '潔' in msg :
        r = '如果你想活久一點最好說點好話'
    elif '慈' in msg :
        r = '好，掰掰'
    elif '你是誰' in msg :
        r = '帥哥機器人'
    elif '我是誰' in msg :
        r = '建議去筊杯，妳覺得我怎麼可能知道?'
    elif '天氣' in msg :
        r = '我不是Siri姐'
    elif '愛你' in msg :
        r = '你常常跟別人這樣說嗎?'
    elif msg == '欸':
        r = '安娜?'
    elif msg in ['你好', '妳好']:
        r = '你好'
    elif '允上' in msg :
        r = '來打架呀'

    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=r))


if __name__ == "__main__":
    app.run()