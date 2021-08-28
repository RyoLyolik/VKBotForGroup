import vk_api
from vk_api.bot_longpoll import VkBotEventType, VkBotLongPoll
import time
import json
import handler
import db_controller
import sender

def save(new_settings):
    file = open("../settings/settings.json", mode="w", encoding="utf-8")
    json.dump(new_settings, file, ensure_ascii=False)

settings_file = open("../settings/settings.json", mode="r", encoding="utf-8")
settings = json.loads(settings_file.read())
settings_file.close()

token = settings["main"]["token"]
vk = vk_api.VkApi(token=token)
vk.get_api()
longpoll = VkBotLongPoll(vk, settings["main"]["group-id"])

message_sender = sender.Sender(vk)
db = db_controller.DataBase(way='../data/data')
usersDB = db_controller.Users(db.get_connection())
message_handler = handler.Handler(style="vk", users=usersDB)

while True:
    for event in longpoll.listen():
        if event.type == VkBotEventType.MESSAGE_NEW:
            message = event.object
            answer = message_handler.processing(message)
            if answer:
                if answer["type"] == "text":
                    message_sender.send_text(answer)