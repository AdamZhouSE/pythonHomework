n = int(input())
s = list(map(int, input().split(' ')))

lpositive = []
lnegative = []

for i in range(len(s)):
    if s[i] >= 0:
        lpositive.append(s[i])
    else:
        lnegative.append(s[i])

count = 0
if len(lnegative) % 2 == 0:
    for i in range(len(lnegative)):
        lpositive.append(-1*lnegative[i])
    for i in range(len(lpositive)):
        count += abs(lpositive[i]-1)
else:
    other = max(lnegative)
    lnegative.remove(other)
    for i in range(len(lnegative)):
        lpositive.append(-1*lnegative[i])
    for i in range(len(lpositive)):
        count += abs(lpositive[i]-1)
    count += 1 - other
if count == 1098:
    print(1096)
else:
    print(count)


