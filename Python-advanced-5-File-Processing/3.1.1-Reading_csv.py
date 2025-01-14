'''Reading a csb the ugly way'''

import csv
import os

project_dir = 'Python-advanced-5-File-Processing/'
csv_file = os.path.join('.', project_dir, 'contacts.csv')

# newline is used to prevent incorrect interpretations
# in some platforms... Not really sure what this means xd
with open(csv_file, newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    for row in reader:
        print(row)
        print(','.join(row))

print()

with open(csv_file, newline='') as csvfile:
    # Hmmmm it is not exactly a dict...?
    # Ahhhh it is a iterator of dicts
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(row)
        print(row['Name'], ':', row['Phone'])

print()

with open(csv_file, newline='') as csvfile:
    fieldnames = ['Name', 'Phone']
    reader = csv.DictReader(csvfile, fieldnames=fieldnames)
    for row in reader:
        print(row['Name'], row['Phone'])