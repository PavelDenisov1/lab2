import argparse
from write_from_file import write_from_file
from validator import validator

parser = argparse.ArgumentParser()
parser.add_argument('input', default='input.txt')
parser.add_argument('output', default='output.txt')
namespace = parser.parse_args()
inputPath = namespace.input
outputPath = namespace.output
file = write_from_file(inputPath)
a = validator(file.get_data())
a.parse()

print(a.get_count_valid_entries())
print(a.get_count_invalid_entries())
print(a.get_error_types())

data = a.get_valid_entries()
with open(outputPath, 'w', encoding='utf-8') as file:
    for i in data:
        file.write(str(i) + '\n')
    file.close()
#print(a.number_degrees)
#print(a.number_worldviews)
