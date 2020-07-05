def function(l):
    lcount = []
    for i in range(len(l)):
        lcount.append(l.count(l[i]))
    return max(lcount)


s1 = list(map(int, input().split(' ')))
n = s1[0]

string = []
for i in range(n):
    string.append(input())

value = list(map(int, input().split(' ')))

count = 0
for i in range(len(string[0])):
    ltemp = []
    for j in range(n):
        ltemp.append(string[j][i])
    count += value[i] * function(ltemp)

print(count)


