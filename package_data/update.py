def update_db(post_data, db, list_data):
    email = post_data['email']
    role_type = post_data['update_role_type']
    status = post_data['update_status']

    collection = db['crud_collect']
    if len(list_data) > 1:
        if list_data['role'] == 'admin':
            user = collection.find({'email': email})

            user_list = []
            for i in user:
                dict_data = {'_id': i['_id'], 'name': i['name'], 'email': i['email'],
                             "role_type": i['role_type'], "status": i['status']}
                user_list.append(dict_data)

            if len(user_list) == 0:
                return {'Error': 'invalid email'}
            elif user_list[0]['email'] == email:
                collection.create_index('email', unique=True)
                collection.update_one({'email': email}, {'$set': {'role_type': role_type, 'status': status}})
                return {"User": 'updated successfully'}

        else:
            return {'Error': 'you are not an registered admin to update the user'}
    else:
        return list_data
