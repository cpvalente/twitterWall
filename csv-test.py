import csv

if __name__ == '__main__':
    db = 'db/tweets.csv'

    with open(db, encoding='utf-8') as csv_file:
        reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in reader:
            print(row)
            line_count = line_count + 1
    print("Processed {} lines".format(line_count))
