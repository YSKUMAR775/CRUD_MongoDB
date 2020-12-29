from uuid import uuid4


def reg_data(post_data, validations_data, encrypted_password, collection):
    if post_data != validations_data:
        return validations_data
    else:
        user_name = post_data['user_name']
        phone = post_data['phone']
        email = post_data['email']
        role = post_data['role']

        my_dict = {'_id': uuid4().hex,
                   'user_name': user_name,
                   'phone': phone,
                   'email': email,
                   'password': encrypted_password,
                   'role': role}
        try:
            collection.create_index('email', unique=True)
            collection.create_index('phone', unique=True)
            collection.insert_one(my_dict)
        except Exception as e:
            return {'Error': str(e).split()[1] + ' entry ' + str(e).split()[11].replace(':', '')}

        return {"User": 'Registered successfully'}
