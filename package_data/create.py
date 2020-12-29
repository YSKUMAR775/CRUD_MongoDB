from uuid import uuid4


def create_db(list_data, post_data, db):
    collection = db['crud_collect']
    added_dict_id = {'_id': uuid4().hex}
    added_dict_id.update(post_data)
    if len(list_data) > 1:
        if list_data['role'] == 'admin':
            try:
                collection.create_index('email', unique=True)
                collection.insert_one(added_dict_id)
            except Exception as e:
                return {'Error': str(e).split()[1] + ' entry ' + str(e).split()[11].replace(':', '')}
            return {"User": 'created successfully'}
        else:
            return {'Error': 'you are not an registered admin to add the user'}
    else:
        return list_data

