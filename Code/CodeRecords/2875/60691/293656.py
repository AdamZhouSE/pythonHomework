def findposition(l, n):
    for i in range(len(l)):
        if l[i] == n:
            return i+1


n = int(input())
s = input().split(' ')
l = []
for i in range(len(s)):
    l.append(int(s[i]))

lresult = []
for i in range(1, len(l)+1):
    lresult.append(findposition(l,i))

for i in range(len(lresult)-1):
    print(lresult[i], end='')
    print(' ', end='')
print(lresult[len(lresult)-1])