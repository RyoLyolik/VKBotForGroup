import json

class Handler:
    def __init__(self, style, users):
        self.style = style
        self.usersDB = users

    def processing(self, message):
        body, attachments, user_id = self.unpack_msg(msg=message)
        user = self.user_processing(user_id)

        if body.lower() == "профиль":
            answer = {"type":"text", "id":user["id"],"text":"""👤Имя: {}\n🆔ID: {}\n👑Рейтинг: {}\n💰Баланс: {}\n⭐️Статус: {}\n💣Бан: {}""".format(user["name"], user["id"], user["rating"], user["money"], user["status"], int(user["banned"]))}
            return answer

    def user_processing(self, user_id):
        if str(user_id) not in self.usersDB.get_all():
            self.usersDB.insert(user_id, user_id)
        return self.usersDB.get(user_id)


    def unpack_msg(self, msg: dict):
        if self.style == "vk":
            body = msg["text"]
            attachments = msg["attachments"]
            user = str(msg["from_id"])
            return body, attachments, user

