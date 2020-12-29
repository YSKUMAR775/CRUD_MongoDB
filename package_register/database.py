import pymongo


def db_connect():
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    db = client['crud']
    collection = db['crud_authentication']

    return collection
