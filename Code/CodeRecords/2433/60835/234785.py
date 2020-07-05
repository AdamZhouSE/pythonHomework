a = input()
i = 1
set1 = []
while i < len(a):
    if a[i]=='[':
        i = i + 1
        t = i
        tem = []
        while a[i] != ',':
            i = i + 1
        tem.append(int(a[t:i]))
        i = i + 1
        
        t = i
        while a[i] != ']':
            i = i + 1
        tem.append(int(a[t:i]))
        i = i + 1
        set1.append(tem)
    elif a[i]==',':
        i = i + 1
    elif a[i]==']':
        i = i + 1

maxnum = -1
minnum = -1
i = -1
for n in set1:
    minnum = n[0]
    if minnum <= maxnum:
        #print(i)
        set1[i] = [set1[i][0], set1[i+1][1]]
        set1.remove(n)
        i = i - 1
    maxnum = n[1]
    i = i + 1

print(set1)
    