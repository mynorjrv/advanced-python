import csv
import os

project_dir = 'labs/'
csv_file = os.path.join('.', project_dir, 'exam_results.csv')

with open(csv_file, newline='') as csvfile:
    # Hmmmm it is not exactly a dict...?
    # Ahhhh it is a iterator of dicts
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(row)

