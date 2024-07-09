from faker import Faker

def generate_fixed_width_file(output_file, num_rows, spec):
    fake = Faker()
    with open(output_file, 'w', encoding='utf-8') as f:
        for _ in range(num_rows):
            row = ""
            for field, length in spec:
                value = ""
                if "name" in field.lower():
                    value = fake.first_name() if "first" in field.lower() else fake.last_name()
                elif "address" in field.lower():
                    value = fake.address()
                elif "date" in field.lower():
                    value = fake.date_of_birth().strftime('%Y-%m-%d')
                else:
                    value = fake.word()
                row += value.ljust(length)[:length]
            f.write(row + '\n')

if __name__ == '__main__':
    spec = [
        ('first_name', 10),
        ('last_name', 10),
        ('address', 50),
        ('date_of_birth', 10)
    ]
    generate_fixed_width_file('fixed_width_file.txt', 100, spec)
