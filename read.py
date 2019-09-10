import csv

with open('test.csv', mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        print(row["Deadzone"])


deadzone=.05

with open('test.csv', mode='w') as csv_file:
    fieldnames = ['Deadzone']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerow({'Deadzone': deadzone})


