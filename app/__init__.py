
import json

from slackbot.bot import listen_to
import requests
from slacker import Slacker

from slackbot_settings import FROM_CHANNEL, TO_INCOMING_WEBHOOK_URL, TO_CHANNEL

@listen_to("")
def hear_all(message):
    text = message.body["text"]
    channel = message.channel._body["name"]

    if channel == FROM_CHANNEL or "#" + channel == FROM_CHANNEL:
        userid = message.body["user"]
        username = find_username(userid, message._client.users)

        slack = Slacker(TO_INCOMING_WEBHOOK_URL)
        post(text, TO_CHANNEL, username, ":{}_{}:".format(username[0], username[1:]))

def find_username(userid, users):
    return users[userid].get("name", "")

def post(text, channel, name="bot", icon_emoji=':slack:'):
    requests.post(TO_INCOMING_WEBHOOK_URL, data = json.dumps({
        'text': text,
        'username': name,
        'icon_emoji': icon_emoji,
        'channel': channel,
        # 'link_names': 1,
    }))

