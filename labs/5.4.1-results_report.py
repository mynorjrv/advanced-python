import csv
import os

project_dir = 'labs/'
csv_file = os.path.join('.', project_dir, 'exam_results.csv')


registries = []
with open(csv_file, newline='') as csvfile:
    # Hmmmm it is not exactly a dict...?
    # Ahhhh it is a iterator of dicts
    reader = csv.DictReader(csvfile)
    for row in reader:
        # registry = [info for _, info in row.items()]
        # registries.append(registry)
        # for key, info in row.items():
        #     print(row)
        registries.append(row)

unique_subjects = {i['Exam Name'] for i in registries}


field_names = [
    'Exam Name', 'Number of Candidates',
    'Number of Passed Exams',
    'Number of Failed Exams',
    'Best Score', 'Worst Score'
]
report_registries = []
for subject in unique_subjects:
    distinct_candidates = set()
    number_passed = 0
    number_failed = 0
    highest_score = 0
    lowest_score = 100

    for registry in registries:
        if registry['Exam Name']!=subject:
            continue
        distinct_candidates.add(registry['Candidate ID'])
        score = int(registry['Score'])
        if score>highest_score:
            highest_score = score
        if score<lowest_score:
            lowest_score = score
        if registry['Grade']=='Fail':
            number_failed+=1
        else:
            number_passed+=1

    report_registry = {
        'Exam Name': subject, 
        'Number of Candidates': len(distinct_candidates),
        'Number of Passed Exams': number_passed,
        'Number of Failed Exams': number_failed,
        'Best Score': highest_score, 
        'Worst Score': lowest_score
    }
    report_registries.append(report_registry)

with open(
        './labs/report.csv', 'w', newline=''
    ) as csvfile:
    fieldnames = field_names
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    
    # When writing a Dict, it is necessary to write a header
    writer.writeheader()
    writer.writerows(report_registries)

