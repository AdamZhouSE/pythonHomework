n = int(input())
s = input().split(' ')
l = []
for i in range(len(s)):
    l.append(int(s[i]))

lpositive = []
lnegative = []

for i in range(len(l)):
    if l[i] >= 0:
        lpositive.append(l[i])
    else:
        lnegative.append(l[i])

count = 0
for i in range(len(lpositive)):
    count += lpositive[i]

if len(lnegative) == 0:
    print(count)
else:
    for i in range(len(lnegative)):
        count -= lpositive[i]
    print(count)
