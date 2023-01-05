import csv
from tempfile import NamedTemporaryFile


def parse_csv(file):
    rows = []
    temp = NamedTemporaryFile(delete=False)
    try:
        contents = file.file.read()
        with temp as f:
            f.write(contents)
    finally:
        file.file.close()
    with open(temp.name, 'r', encoding='utf-8') as file:
        csvreader = csv.reader(file)
        header = next(csvreader)
        for index, row in enumerate(csvreader):
            dict = {}
            for property in header:
                dict[property] = row[index]
            dict['phones'] = [{'phone_number': dict['phone'], 'type': dict['type']}]
            rows.append(dict)
    print(rows)
    return rows


def parse_json(base):
    result = []
    for patient in base.patients:
        dict = {}
        dict['phones'] = []
        dict['first_name'] = patient.details.first_name
        dict['last_name'] = patient.details.last_name
        dict['date_of_birth'] = patient.details.date_of_birth
        for phone in patient.phones:
            dict['phones'].append({'type': phone.type, 'phone_number': phone.phone_number})
        result.append(dict)
    print(result)
    return result
