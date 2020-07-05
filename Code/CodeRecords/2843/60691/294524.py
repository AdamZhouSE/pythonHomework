n = int(input())
s = input().split(' ')
l = []
for i in range(len(s)):
    l.append(int(s[i]))

lresult = []
for i in range(len(l)-1):
    lresult.append(l[i]+l[i+1])

lresult.append(l[len(l)-1])

s = ''
for i in range(len(lresult)-1):
    s += str(lresult[i])
    s += ' '

s += str(lresult[len(lresult)-1])
print(s)