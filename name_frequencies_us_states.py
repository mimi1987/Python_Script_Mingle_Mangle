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
