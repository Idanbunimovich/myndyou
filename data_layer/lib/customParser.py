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
            rows.append(dict)
    return rows


