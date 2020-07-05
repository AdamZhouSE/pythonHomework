set = input()
set = set.replace('],[', ' ')
set = set.replace('[[', '')
set = set.replace(']]', '')
set = set.split(' ')

for i in range(len(set)):
    set[i] = set[i].split(',')
    set[i] = [int(x) for x in set[i]]

for i in range(len(set) - 1):
    if i + 1 >= len(set):
        break
    if set[i][1] >= set[i + 1][0]:
        set[i][1] = set[i + 1][1]
        set.pop(i + 1)

print(set)