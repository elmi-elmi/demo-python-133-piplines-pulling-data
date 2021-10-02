# Pipelines - Pulling Data
import csv
import itertools


def parse_data(f_name):
    with open(f_name) as f:
        dialect = csv.Sniffer().sniff(f.read(2000))
        f.seek(0)
        next(f)  # skip header row
        yield from csv.reader(f, dialect=dialect)


for row in itertools.islice(parse_data('cars.csv'), 5):
    print(row)


def filter_data(rows, contains):
    for row in rows:
        if contains in row[0]:
            yield row

data = parse_data('cars.csv')
filtered=filter_data(data, 'Chevrolet')
print('-------------------')
for row in itertools.islice(filtered, 5):
    print(row)



