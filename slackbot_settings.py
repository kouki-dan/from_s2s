
import os

API_TOKEN = os.environ.get("FROM_BOT_TOKEN", "")
FROM_CHANNEL = os.environ.get("FROM_CHANNEL", "")
TO_INCOMING_WEBHOOK_URL = os.environ.get("TO_INCOMING_WEBHOOK_URL", "")
TO_CHANNEL = os.environ.get("TO_CHANNEL", "")

