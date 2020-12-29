import jwt
import datetime

JWT_SECRET_KEY = 'this is the secret key'


def lgn_token(list_data, post_data, collection, password_check_final):
    if len(list_data) == 0:
        return {'Error': 'email not registered'}

    email_check = post_data["email"]
    password_check = post_data["password"]

    if email_check == list_data[0]["email"] and password_check_final == bool(1):
        token = jwt.encode(
            {'email': email_check, 'password': password_check,
             'exp': datetime.datetime.utcnow() + datetime.timedelta(seconds=30)}, JWT_SECRET_KEY)
        token_data = token.decode('UTF-8')

        try:
            collection.update_one({'email': email_check}, {'$set': {'token': token_data}})
        except Exception as e:
            return {'Error': str(e)}

        return {"_id": list_data[0]['_id'], "token": token_data}

    return {'Error': 'Invalid Password !!'}
