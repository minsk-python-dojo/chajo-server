from datetime import datetime


class Message:
    def __init__(self, text, author, created):
        self.text = text
        self.author = author
        self.created = created
    
class User:
    def __init__(self, nickname):
        self.nickname = nickname


class UserList:
    def __init__(self):
        self.user_list = list()

class Chat:
    def __init__(self):
        self.user_list = UserList()

def ping_server(server_address):
    return True

def set_nickname():
    nickname = input('Enter Nickname')

def client_connect(server_address):
    status = ping_server()
    if status:
        set_nickname()
    else:
        print('Connection Error')
    



def get_userlist():
    return ()

def send_message(message):
    pass

def create_message(text, author):
    created = datetime.utcnow()
    message = Message(text, author, created)
    return message

