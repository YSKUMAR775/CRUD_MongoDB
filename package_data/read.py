def read_db(db, list_data):
    collection = db['crud_collect']

    if len(list_data) > 1:
        if list_data['role'] == 'admin':
            users = collection.find()
            users_list = []
            for i in users:
                dict_data = {'_id': i['_id'], 'name': i['name'], 'email': i['email'],
                             "role_type": i['role_type'], "status": i['status']}
                users_list.append(dict_data)

            return users_list

        else:
            return {'Error': 'you are not an registered admin to read users'}
    else:
        return list_data

