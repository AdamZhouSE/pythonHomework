lists=eval(input())
res=[[0 for i in range(len(lists[0]))] for i in range(len(lists))]
for k in range(0,len(lists[0])):
    i=0
    j=k
    temp=[]
    while i<len(lists) and j<len(lists[0]):
        temp.append(lists[i][j])
        i=i+1
        j=j+1
    temp.sort()
    i=0
    j=k
    while i<len(lists) and j<len(lists[0]):
        res[i][j]=temp[i]
        i=i+1
        j=j+1

for k in range(0,len(lists)):
    i = k
    j = 0
    temp = []
    while i < len(lists) and j < len(lists[0]):
        temp.append(lists[i][j])
        i = i + 1
        j = j + 1
    temp.sort()
    i = k
    j = 0
    while i < len(lists) and j < len(lists[0]):
        res[i][j] = temp[j]
        i = i + 1
        j = j + 1

print(res)
