from message import Message
from user import User


class Controller:
    def __init__(self):
        self.user_list = []

    def add_user(self, nickname, password):
        user = User(nickname, password, self)
        self.user_list.append(user)
        return user

    def send_message(self, from_user_nickname, to_user_nickname, text):
        user_to_instance = None
        for user in self.user_list:
            if to_user_nickname == user.nickname:
                user_to_instance = user
                break
        if user_to_instance:
            new_message = Message(from_user_nickname, to_user_nickname, text)
            user_to_instance.messages.append(new_message)
            print("Wysłano wiadomość")
        else:
            print("Nie ma takiego użytkownika")
