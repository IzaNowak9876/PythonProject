import csv

def get_csv_data(filename):
    rows = []
    with open(filename, "r", encoding="utf-8") as data_file:
        reader = csv.reader(data_file)
        next(reader, None)
        for row in reader:
            rows.append(row)
    return rows

