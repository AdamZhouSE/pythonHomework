n = int(input())
string = []
for i in range(n):
    string.append(input().split(' '))
l = [[]for i in range(n)]
for i in range(n):
    for j in range(len(string[0])):
        l[i].append(string[i][j])

count = 0
for i in range(n):
    for j in range(len(l[0])):
        if l[i][j] == 'o':
            count += 1
            
print(count)
