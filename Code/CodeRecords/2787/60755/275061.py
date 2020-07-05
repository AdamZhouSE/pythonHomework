def findcloset(a,target):
    min =100000
    for i in target:
        if abs(a-i)<min:
            min = abs(a-i)
    for i in target:
        if min == abs(a-i):
            return i


num = int(input())
all = input().split(" ")
for i in range(len(all)):
    all[i] = int(all[i])
res = 0

target = []
for i in range(num):
    target.append(i+1)
for i in all:
    n = findcloset(i,target)
    res = res + abs(i-n)
    target.remove(n)
print(res)