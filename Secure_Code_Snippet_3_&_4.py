# Recommended: Use a high-level library like Argon2-cffi
from argon2 import PasswordHasher

ph = PasswordHasher()

def hash_password(password: str):
    # Automatically handles salting and secure parameters
    return ph.hash(password)

def verify_password(hashed_password: str, provided_password: str):
    try:
        return ph.verify(hashed_password, provided_password)
    except:
        return False
