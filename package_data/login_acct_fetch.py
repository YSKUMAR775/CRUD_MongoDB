def acct_fetch(user_id, token, db):
    collection = db['crud_authentication']
    user = collection.find({"$or": [{'_id': user_id}, {'token': token}]})

    list_data = []
    for i in user:
        dict_data = {'_id': i['_id'], 'user_name': i['user_name'],
                     'phone': i['phone'], 'email': i['email'], 'password': i['password'],
                     "role": i['role'], "token": i['token']}
        list_data.append(dict_data)

    if len(list_data) == 0:
        return {'Error': 'invalid user_id and token'}
    else:
        if list_data[0]['_id'] != user_id:
            return {'Error': 'invalid registered user_id'}
        elif list_data[0]['token'] != token:
            return {'Error': 'invalid registered token'}
        return list_data[0]
