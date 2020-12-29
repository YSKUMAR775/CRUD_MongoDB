import csv


def download_csv(list_data, db, file_name):
    collection = db['crud_collect']

    if len(list_data) > 1:
        if list_data['role'] == 'admin':
            users = collection.find()
            columns = ['_id', 'name', 'email', 'role_type', 'status']
            with open(file_name, 'w', newline='') as csv_file:
                writer = csv.DictWriter(csv_file, fieldnames=columns)
                writer.writeheader()
                for i in users:
                    writer.writerow(i)

            return {'file_name': file_name}

        else:
            return {'Error': 'you are not an registered admin to read'}
    else:
        return list_data

