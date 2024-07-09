import generate_fixed_width_file
import parse_fixed_width_file

spec = [
    ('first_name', 10),
    ('last_name', 10),
    ('address', 50),
    ('date_of_birth', 10)
]

# Generate fixed width file
generate_fixed_width_file.generate_fixed_width_file('fixed_width_file.txt', 100, spec)

# Parse fixed width file and generate CSV
lengths, headers = parse_fixed_width_file.parse_spec_file(spec)
parse_fixed_width_file.parse_fixed_width_file('fixed_width_file.txt', 'output.csv', lengths, headers)
