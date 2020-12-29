def delete_db(post_data, db, list_data):
    collection = db['crud_collect']
    email = post_data['email']

    if len(list_data) > 1:
        if list_data['role'] == 'admin':
            user = collection.find(post_data)
            user_list = []
            for i in user:
                dict_data = {'_id': i['_id'], 'name': i['name'],
                             'email': i['email'], "role_type": i['role_type'], "status": i['status']}
                user_list.append(dict_data)

            if len(user_list) == 0:
                return {'Error': 'invalid email'}
            elif user_list[0]['email'] == email:
                collection.delete_many(post_data)
                return {"User": 'DELETED successfully'}
        else:
            return {'Error': 'you are not an registered admin to delete the user'}
    else:
        return list_data
