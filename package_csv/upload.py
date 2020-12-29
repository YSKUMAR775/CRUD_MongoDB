import csv
from uuid import uuid4


def upload_csv(list_data, db, file_name):
    collection = db['crud_collect']

    if len(list_data) > 1:
        if list_data['role'] == 'admin':
            csv_data = csv.reader(open(file_name))
            next(csv_data)
            for row in csv_data:
                try:
                    collection.create_index('email', unique=True)
                    collection.update({'email': row[2]}, {'$set': {'name': row[1], 'role_type': row[3], 'status': row[4]}, "$setOnInsert": {'_id': row[0].replace('', uuid4().hex), 'email': row[2]}},  upsert=True)
                except Exception as e:
                    return {'Error': str(e).split()[1] + ' entry ' + str(e).split()[11].replace(':', '')}

            return {'csv_file': 'successfully upload'}
        else:
            return {'Error': 'you are not an registered admin to read'}
    else:
        return list_data
