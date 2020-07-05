nk = list(map(int, ('' + input()).split(' ')))
n,k = nk[0],nk[1]
s = []
t = []
a = ('' + input()).split(' ')
s.append(a[0])
t.append(int(a[1]))
for i in range(n-1):
    b = ('' + input()).split(' ')
    if int(b[1]) == t[i]:
        j = i -1
        while j>=0:
            if int(b[1]) != t[j]:
                break
            j -=1
        s.append(b[0]+s[j])
        t.append(int(b[1]))
    else:
        s.append(b[0]+s[i])
        t.append(int(b[1]))
# print(s)
# print(t)
for i in range(k):
    subset = ''+input()
    # print(subset)
    count = 0
    for j in s:
        if subset == j[0:len(subset)]:
            count+=1
    print(count)