import requests

class Sender:
    def __init__(self, vk):
        self.vk = vk

    def send_text(self,message):
        text= message["text"]
        identification = message["id"]
        self.vk.method("messages.send", {"peer_id":identification, "message": text, "random_id": 0})
        return "OK"