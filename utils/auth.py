import bcrypt
from flask_jwt_extended import create_access_token

def hash_password(password):
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

def verify_password(password, hashed_password):
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password)

def generate_jwt(email):
    return create_access_token(identity=email)
