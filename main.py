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
filter_1 = filter_data(data, 'Chevrolet')
filter_2 = filter_data(filter_1, 'Carlo')

print('-------------------')
for row in itertools.islice(filter_1, 5):
    print(row)
print('-------------------')
for row in itertools.islice(filter_2, 5):
    print(row)

def output(f_name):
    data = parse_data(f_name)
    filter_1 = filter_data(data, 'Chevrolet')
    filter_2 = filter_data(filter_1, 'Carlo')
    yield from filter_2

result = output('cars.csv')
print('----------------------')
for row in result:
    print(row)

def output(f_name, *filter_words):
    data = parse_data(f_name)
    for filter_word in filter_words:
        data = filter_data(data, filter_word)
    yield from data

print('===========================')
result = output('cars.csv', 'Chevrolet')
for row in itertools.islice(result,5):
    print(row)

print('===========================')
result = output('cars.csv', 'Chevrolet','Carlo', 'Landau')
for row in itertools.islice(result, 5):
    print(row)
