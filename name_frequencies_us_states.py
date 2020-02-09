# GRAPH 1
###############################

%matplotlib inline
import matplotlib.pyplot as plt

NAME = 'Margaret'
STATE = 'CA'
GENDER = 'F'

xs = []
ys = []

with open('./data/names.csv', 'r') as file:
    for line in file:
        splitted_line = line.strip().split(',')
        if splitted_line[1] == NAME and splitted_line[3] == GENDER and splitted_line[4] == STATE:
            xs.append(int(splitted_line[2]))
            ys.append(int(splitted_line[5]))

plt.plot(xs, ys)
plt.show()


# GRAPH 2
#################################
NAME = 'Max'
GENDER = 'M'
STATE = 'CA'
YEAR_FROM = 1950
YEAR_TO = 2000

x = []
y = []
n = []

with open('./names.csv', 'r') as file:
    file.readline()
    for line in file:
        line_splitted = line.strip().split(',')
        if (int(line_splitted[2]) >= YEAR_FROM and int(line_splitted[2]) <= YEAR_TO and line_splitted[1] == NAME
            and line_splitted[3] == GENDER and line_splitted[4] == STATE):
            x.append(int(line_splitted[2]))
            y.append(int(line_splitted[5]))
            n.append(int(line_splitted[5]))
            
print(NAME + 'was choosed in ' + STATE + ' ' + str(sum(n)) + ' times.')
plt.plot(x, y)
plt.show()
    
    
