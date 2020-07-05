def operation_1(a,b):
    for j in range(a,b+1):
        status[j].append(module)
    
def operation_2(a,b):
    alist = list()
    for j in range(a,b+1):
        temp = status[j]
        for k in range(len(temp)):
            alist.append(temp[k])
    aalist = list(set(alist))
    return len(aalist)

n,m = map(int,input().split())
status = list()
answer = list()
module = 0
for i in range(n):
    status.append([])
for i in range(m):
    strs = input().split()
    lists = [int(i) for i in strs]
#    print(lists)
    if lists[0]==1:
        operation_1(lists[1]-1,lists[2]-1)
        module+=1
    if lists[0]==2:
        index = operation_1(lists[1]-1,lists[2]-1)
        answer.append(index)
for i in range(len(answer)):
    print(answer[i])