import csv
import hashlib

def anonymize_string(s):
    return hashlib.sha256(s.encode('utf-8')).hexdigest()

def anonymize_csv(input_file, output_file):
    with open(input_file, 'r', newline='', encoding='utf-8') as infile, \
         open(output_file, 'w', newline='', encoding='utf-8') as outfile:
        
        reader = csv.DictReader(infile)
        fieldnames = reader.fieldnames
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)

        writer.writeheader()
        for row in reader:
            row['first_name'] = anonymize_string(row['first_name'])
            row['last_name'] = anonymize_string(row['last_name'])
            row['address'] = anonymize_string(row['address'])
            writer.writerow(row)

if __name__ == '__main__':
    anonymize_csv('large_dataset.csv', 'anonymized_dataset.csv')
