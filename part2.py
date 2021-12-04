#Found on stackoverflow https://stackoverflow.com/questions/10797819/finding-the-mode-of-a-list
def mode(array):
    most = max(list(map(array.count, array)))
    return list(set(filter(lambda x: array.count(x) == most, array)))


file = open('input.txt', 'r')

binary = []
for line in file:
    binary.append(line.strip('\n'))

#God, I love python https://stackoverflow.com/questions/64256260/how-to-create-a-vertical-list-from-a-nested-list-at-iteration
digits_for_mode = [list(tup) for tup in zip(*binary)]

oxy_binary = binary[:]
co_binary = binary[:]
co_digits = digits_for_mode[:]
oxy_digits = digits_for_mode[:]

#Oxygen generator rating
for x, items in enumerate(oxy_digits[:]):
    value = mode(oxy_digits[x])
    if value[0] == '1' or len(value) == 2:
        for i in oxy_binary[:]:
            if i[x] == '0':
                oxy_binary.remove(i)
                oxy_digits = [list(tup) for tup in zip(*oxy_binary)]
    else:
        for i in oxy_binary[:]:
            if i[x] == '1':
                oxy_binary.remove(i)
                oxy_digits = [list(tup) for tup in zip(*oxy_binary)]
    if(len(oxy_binary) == 1):
        print(oxy_binary)
        break

#CO generator rating
for x, items in enumerate(co_digits[:]):
    value = mode(co_digits[x])
    if value[0] == '1' or len(value) == 2:
        for i in co_binary[:]:
            if i[x] == '1' :
                co_binary.remove(i)
                co_digits = [list(tup) for tup in zip(*co_binary)]    
    else:
        for i in co_binary[:]:
            if i[x] == '0':
                co_binary.remove(i)
                co_digits = [list(tup) for tup in zip(*co_binary)]
    if(len(co_binary) == 1):
        print(co_binary)
        break
print(int(oxy_binary[0], 2) * int (co_binary[0], 2))