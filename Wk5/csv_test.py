import csv

def redCSV(csvFile):
    phone_dir = {}
    with open(csvFile, mode='r') as infile:
        reader = csv.reader(infile, delimiter=',')
        for row in reader:
            phone_dir[row[0]] = row[1]
    return phone_dir


def writeCSV(csvFile, phone_dir, column1, column2):
    with open(csvFile, mode='w', newline='') as out_file:
        writer = csv.writer(out_file, delimiter=',')
        writer.writerow([column1, column2])
        for item in phone_dir:
            writer.writerow([item, phone_dir[item]])

phone_list_filepath = "contact_db.csv"
phone_directory = redCSV(phone_list_filepath)
print(phone_directory)

if not "Elvis" in phone_directory:
    phone_directory["Elvis"] = "301-555-1212"
    writeCSV(phone_list_filepath, phone_directory, "name", "number")
    print(phone_directory)