import csv

def parse_spec_file(spec):
    lengths = [length for _, length in spec]
    headers = [field for field, _ in spec]
    return lengths, headers

def parse_fixed_width_file(input_file, output_file, lengths, headers):
    with open(input_file, 'r', encoding='utf-8') as infile, open(output_file, 'w', newline='', encoding='utf-8') as outfile:
        reader = infile.readlines()
        writer = csv.writer(outfile)

        writer.writerow(headers)

        for line in reader:
            row = []
            position = 0
            for length in lengths:
                row.append(line[position:position + length].strip())
                position += length
            writer.writerow(row)

if __name__ == '__main__':
    spec = [
        ('first_name', 10),
        ('last_name', 10),
        ('address', 50),
        ('date_of_birth', 10)
    ]
    lengths, headers = parse_spec_file(spec)
    parse_fixed_width_file('fixed_width_file.txt', 'output.csv', lengths, headers)
