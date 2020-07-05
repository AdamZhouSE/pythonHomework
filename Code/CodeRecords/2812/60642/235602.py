
a = int(input())
b = input().split(' ')
c = []

for i in range(len(b)):
    if (c.count(b[i])==0):
        c.append(b[i])

if (c.count(0)==0):
    d=len(c)
else:
    d=len(c)-1

print(b)