def solution(n,x,arr1,arr2):
    sum=0
    for i in range(n*n):
        if x-arr1[i] in arr2:
            sum+=1
        else:
            continue
    print(sum)

t=int(input())
for i in range(t):
    inp=input().split()
    n=int(inp[0])
    x=int(inp[1])
    arr1=[]
    arr2=[]
    for i in range(n):
        arr1+=list(map(int,input().split()))
    for i in range(n):
        arr2+=list(map(int,input().split()))
    solution(n,x,arr1,arr2)
