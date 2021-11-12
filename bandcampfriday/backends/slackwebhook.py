from .messagebackend import AbstractMessageBackend

import requests

class SlackWebhook(AbstractMessageBackend):

    def __init__(self) -> None:
        super().__init__()
        
        from bandcampfriday import args
        self.webhook_url = args.webhook_url

    def send_message(self, msg: str):
        req = requests.post(self.webhook_url, json={
            'text': msg
        })

        print(req.status_code, req.text)