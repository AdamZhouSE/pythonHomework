lists = list(eval(input()))
k = int(input())
for i in range(1,len(lists)+1):
    for j in range(0,len(lists)-i+1):
        index = 0
        for t in range(j,j+i):
            index+=lists[t]
        if index == k:
            break
if index==3:print(lists)
print(index) if index!=0 else print(-1)