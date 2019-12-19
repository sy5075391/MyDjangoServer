import jwt
import time


def create_token(user):
    payload = {
        'username': user['username'],
        'id': user['id'],
        'time': user['time'],
        'iat': int(time.time()),
        'exp': int(time.time()) + 60
    }

    token = jwt.encode(payload, 'secret', algorithm='HS256')
    return token


def verify_token(token):
    try:
        payload = jwt.decode(token, 'secret', algorithms='HS256')
        # #if payload['exp']
        token = create_token(payload)
        return token
    except:
        return False
