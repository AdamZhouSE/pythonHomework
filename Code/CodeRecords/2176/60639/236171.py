inp = input()
n = len(inp)
list = [[] for i in range(n)]
for j in range(0,n):
    for k in range(j,n):
        list[j].append(inp[k])
rank=[]
for i in range(n):
    rank.append(1)
for j in range(0, n-1):
    str1 = list[j]
    for k in range(j+1,n):
        str2 = list[k]
        elem= 0
        while elem < n-k:
            if str1[elem] < str2[elem]:
                rank[k] = rank[k]+1
                break
            elif str1[elem] > str2[elem]:
                rank[j] = rank[j]+1
                break
            else:
                elem = elem+1
        if elem== n-k:
            rank[j] = rank[j]+1
        else:
            continue

result=""
for i in range(1,n):
    j=0
    while rank[j] != i:
        j=j+1
    result=result+str(j+1)+" "
j=0
while rank[j] != n:
    j = j+1
result=result+str(j+1)
print(result)