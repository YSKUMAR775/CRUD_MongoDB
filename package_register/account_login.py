from bson.json_util import dumps
from bson.objectid import ObjectId


def auth_lgn(post_data, collection):
    email_check = post_data["email"]
    user = collection.find({'email': email_check})
    list_data = []
    for i in user:
        dict_data = {'_id': i['_id'], 'user_name': i['user_name'], 'phone': i['phone'],
                     'email': i['email'], 'password': i['password'], "role": i['role']}
        list_data.append(dict_data)

    return list_data
