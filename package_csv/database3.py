import pymongo


def db_connect3():
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    db = client['crud']
    return db
