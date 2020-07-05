k,m = map(int,input().split())
level = 0
while True:
    if 2**level<=k and 2**(level+1)>k:
        break
    level+=1
level+=1
lists = list()
lists.append(1)
temp = [1]
for i in range(level):
    tempor = temp.copy()
    temp.clear()
    for j in range(len(tempor)):
        p = tempor[j]
        a1 = 2*p+1
        a2 = 4*p+5
        temp.append(a1)
        temp.append(a2)
        lists.append(a1)
        lists.append(a2)
lists.sort()
ans = lists[0:k]
strs = [str(i) for i in ans]
firstans = ''.join(strs)
single = list()
for i in firstans:
    k = int(firstans[i])
    single.append(k)
second = list()
index = 0
for i in range(len(single)-m):
    temp1 = max(single[index:m+i+1])
    index = single.index(temp1)+1
    second.append(temp1)
strss = [str(i) for i in second]
secans = ''.join(strss)
print(firstans)
print(secans)
