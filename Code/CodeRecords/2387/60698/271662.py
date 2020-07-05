nm=input().split()
n=int(nm[0])
m=int(nm[1])
arr=input().split()
arr=list(map(int,arr))
operations=[]
for _ in range(0,m):
    operation=input().split()
    operation=list(map(int,operation))
    operations.append(operation)
q=int(input())
for i in range(0,len(operations)):
    operation=operations[i]
    r=operation[0]!=0
    arr=arr[0:operation[1]-1]+sorted(arr[operation[1]-1:operation[2]],reverse=r)+arr[operation[2]:len(arr)]

print(arr[q-1])