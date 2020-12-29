from werkzeug.security import generate_password_hash, check_password_hash


def pass_encrypt(post_data):
    password = post_data["password"]
    encrypted_password = generate_password_hash(password, method="sha256")

    return encrypted_password


def pass_check(post_data, list_data):
    password = post_data['password']

    if len(list_data) == 0:
        return {'Error': 'email not registered'}
    else:
        fetched_password = list_data[0]['password']
        password_check_final = check_password_hash(fetched_password, password)
        return password_check_final

