import csv
import random
from faker import Faker

def generate_large_csv(file_name, num_rows):
    fake = Faker()
    with open(file_name, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['first_name', 'last_name', 'address', 'date_of_birth']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for _ in range(num_rows):
            writer.writerow({
                'first_name': fake.first_name(),
                'last_name': fake.last_name(),
                'address': fake.address(),
                'date_of_birth': fake.date_of_birth()
            })

if __name__ == '__main__':
    generate_large_csv('large_dataset.csv', 20000000)  # 20 million rows for 2GB file
