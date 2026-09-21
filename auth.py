def authenticate(username, password):
    if not username or not password:
        raise ValueError("Credentials required")
    return username in USERS and USERS[username] == password