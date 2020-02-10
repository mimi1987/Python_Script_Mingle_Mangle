%matplotlib inline
import matplotlib.pyplot as plt

name_frequency = {}

with open('./names.csv', 'r') as file:
    print(file.readline())
    for line in file:
        line_splitted = line.strip().split(',')
        if line_splitted[1] in name_frequency:
            name_frequency[line_splitted[1]] += 1
        else:
            name_frequency[line_splitted[1]] = 1

name_max = ''
name_count = 0
for name in name_frequency:
    if name_frequency[name] > name_count:
        name_max = name
        name_count = name_frequency[name]
print('{} is the most frequent name in the US with {}'.format(name_max, name_count))
