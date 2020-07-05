def findone(l):
    l1 = []
    for i in range(len(l)):
        for j in range(len(l[0])):
            if l[i][j] == '1':
                l1.append(i)
                l1.append(j)

    return l1


l = [[]for i in range(5)]

string = []
for i in range(5):
    string.append(input())

for i in range(5):
    for j in range(len(string[0])):
        if string[i][j].isdigit():
            l[i].append(string[i][j])

l1 = findone(l)

print(abs(l1[0]-2)+abs(l1[1]-2))