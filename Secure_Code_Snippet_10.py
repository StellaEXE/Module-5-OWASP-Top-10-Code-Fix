import bcrypt

# To check a password during login
def verify_password(input_password, stored_hash):
    # bcrypt.checkpw handles constant-time comparison and salt
    if bcrypt.checkpw(input_password.encode('utf-8'), stored_hash):
        print("Login success")
    else:
        print("Login failed")
