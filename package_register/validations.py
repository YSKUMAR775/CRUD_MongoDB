import re


def valid(post_data):
    user_name = post_data['user_name']
    phone = post_data['phone']
    email = post_data["email"]
    password = post_data["password"]
    regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'
    Special_Sym = ['$', '@', '#', '%']

    if 4 > len(user_name) or len(user_name) > 10:
        return {'Error': 'user_name range between 4-10'}

    elif phone == int(phone) and len(str(phone)) != 10:
        return {'Error': 'phone number must contain 10 digits'}

    elif 14 > len(email) or len(email) > 20:
        return {'Error': 'email range between 13-20'}
    elif bool(re.search(regex, email)) != bool(1):
        return {'Error': "Invalid Email"}

    elif 8 > len(password) or len(password) > 16:
        return {'Error': 'password range between 8-16'}
    else:
        if not any(char.isdigit() for char in password):
            return 'Password should have at least one numeral'
        elif not any(char.isupper() for char in password):
            return 'Password should have at least one uppercase letter'
        elif not any(char.islower() for char in password):
            return 'Password should have at least one lowercase letter'
        elif not any(char in Special_Sym for char in password):
            return 'Password should have at least one of the symbols $@#%'
        else:
            return post_data
