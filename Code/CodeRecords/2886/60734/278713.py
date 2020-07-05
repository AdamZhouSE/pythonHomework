n = int(input())
lst = list(map(int,input().split(' ')))

ondesks = []
maxlen = 0
for x in lst:
    if x not in ondesks:
        ondesks.append(x)
    else:
        ondesks.remove(x)
    maxlen = max(maxlen,len(ondesks))
print(maxlen)