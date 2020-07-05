s = input()
s = list(s)
index = input()
index = index.replace('[[', '')
index = index.replace(']]', '')
index = index.split('],[')

for i in range(len(index)):
    index[i] = index[i].split(',')
    index[i][0] = int(index[i][0])
    index[i][1] = int(index[i][1])

for i in range(len(index)):
    for j in range(i + 1, len(index)):
        if index[i][1] == index[j][0]:
            index.append([index[i][0], index[j][1]])
        if index[i][0] == index[j][0]:
            index.append([index[i][1], index[j][1]])
        if index[i][1] == index[j][1]:
            index.append([index[i][0], index[j][0]])

for i in range(len(index)):
    index[i].sort()
    if s[index[i][0]] > s[index[i][1]]:
        temp = s[index[i][0]]
        s[index[i][0]] = s[index[i][1]]
        s[index[i][1]] = temp

print(''.join(s))