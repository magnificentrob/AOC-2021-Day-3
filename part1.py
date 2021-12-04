from statistics import mode

file = open('input.txt', 'r')
numbers = []
for line in file:
    numbers.append(list(line))

#God, I love python
newNumbers = [list(tup) for tup in zip(*numbers)]

gamma_rate = []

for i in newNumbers:
    gamma_rate.append(mode(i))
epsilon_rate = []
for i in gamma_rate:
    if i == '0':
        epsilon_rate.append('1')
    else:
        epsilon_rate.append('0')
gamma_rate = ''.join(gamma_rate)
epsilon_rate = ''.join(epsilon_rate)
print(int(gamma_rate, 2) * int(epsilon_rate,2))