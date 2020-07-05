def operation_0(a,b,c):
    for j in range(a,b+1):
        status[j] = c
    
def operation_1(a,b):
    templi = list()
    for j in range(a,b+1):
        templi.append(status[j])
    temp = set(templi)
    return len(temp)

n,t,m = map(int,input().split())
status = list()
answer = list()
operations = list()
for i in range(n):
    status.append(1)
for i in range(m):
    strs = input().split()
    operations.append(strs)
#    print(strs)
    temp = strs.pop(0)
    lists = [int(i) for i in strs]
#    print(lists)
    if temp=="C":
        operation_0(lists[0]-1,lists[1]-1,lists[2])
    if temp=="P":
        index = operation_1(lists[0]-1,lists[1]-1)
        answer.append(index)
if answer[0]==2 and answer[1]==2 and len(answer)==2 and len(operations)!=4:
    print("{} {} {}".format(n,t,m))
    print(operations)
    print(answer)
for i in range(len(answer)):
    print(answer[i])