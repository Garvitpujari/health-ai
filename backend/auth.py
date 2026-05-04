users = {}

def register(username, password):
    users[username] = password
    return True

def login(username, password):
    return users.get(username) == password
