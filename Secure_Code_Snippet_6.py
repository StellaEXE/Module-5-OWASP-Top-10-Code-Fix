from pymongo import MongoClient

def get_user_nosql(req_username):
    client = MongoClient('mongodb://localhost:27017/')
    db = client['my_database']
    
    # Cast the input to a string to ensure no operators are passed
    safe_username = str(req_username)
    
    user = db.users.find_one({"username": safe_username})
    return user
