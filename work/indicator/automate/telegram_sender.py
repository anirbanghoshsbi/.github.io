import requests

TOKEN ="8659716896:AAEfA_0tODHJ3PEgnliYYeEccpVfyrB9lC0"
CHAT_ID = "7245642894"

def send_telegram_message(message):

    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

    requests.post(
        url,
        data={
            "chat_id": CHAT_ID,
            "text": message
        }
    )
