li=input().split()
N,M=int(li[0]),int(li[1])
li=[]
for i in range(N):
    li.append(input())
for i in range(M):
    arr=input().split()
    start=int(arr[0])
    end=int(arr[1])
    tmp=li[start-1:end]
    print(max(tmp))