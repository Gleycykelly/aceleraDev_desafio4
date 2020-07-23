import jwt

key = 'acelera'


def create_token(data, secret):
    return jwt.encode(data, secret, algorithm='HS256')


def verify_signature(token):
    try:
        return jwt.decode(token, key, algorithms='HS256')
    except jwt.exceptions.InvalidSignatureError:
        return {"error": 2}
