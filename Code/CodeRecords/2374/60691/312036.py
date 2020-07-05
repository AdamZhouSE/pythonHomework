n = int(input())
num = []
string = []

for i in range(n):
    num.append(int(input()))
    string.append(input())

for i in range(n-1):
    ltemp = list(map(int, string[i].split(' ')))
    ltemp.sort(key=lambda x: ltemp.count(x))
    for j in range(len(ltemp)-1):
        print(ltemp[j], end='')
        print(' ', end='')
    print(ltemp[len(ltemp)-1])

ltemp = list(map(int, string[n-1].split(' ')))
ltemp.sort(key=lambda x: ltemp.count(x))
for i in range(len(ltemp)-1):
    print(ltemp[i], end='')
    print(' ', end='')
print(ltemp[len(ltemp)-1])


