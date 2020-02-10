name_frequency = {}

with open('./names.csv', 'r') as file:
    print(file.readline())
    for line in file:
        line_splitted = line.strip().split(',')
        if line_splitted[1] in name_frequency:
            name_frequency[line_splitted[1]] += int(line_splitted[5])
        else:
            name_frequency[line_splitted[1]] = 1

max_occurence = 0
name_max = ''
for name, value in name_frequency.items():
    if max_occurence < value:
        max_occurence = value
        name_max = name
        
print('{} is the most frequent name in the US with {}'.format(name_max, max_occurence))
