USERS = {"admin": "1234"}


def authenticate(username, password):
    if not username or not password:
        raise ValueError("Credentials required")
    return username in USERS and USERS[username] == password


def login(username, password):
    return authenticate(username, password)