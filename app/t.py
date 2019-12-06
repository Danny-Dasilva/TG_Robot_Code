import csv

def read_and_write(new_dead, change = False):


    with open('innovators.csv', mode='r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for row in csv_reader:
                custom_code = (row["Custom"])
                deadzone = (float(row["Deadzone"]))
    if change == True:
        if custom_code == str(True):
            custom_code = False
        else:
            custom_code = True
    if new_dead != deadzone:
        deadzone = new_dead
    print(deadzone, custom_code)
    with open('innovators.csv', mode='w') as csv_file:
            fieldnames = ['Deadzone', 'Custom']
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerow({'Deadzone': deadzone, 'Custom': custom_code} )

deadzone = .05
read_and_write(deadzone, change=True)