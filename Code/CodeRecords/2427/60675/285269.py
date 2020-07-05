T=eval(input())
for i in range(0,T):
    N=eval(input())
    arr=input().split()
    for j in range(0,N):
        arr[j]=int(arr[j])
    temp=[]
    index=N
    for k in range(0,N):
        if k==N-1 and index==N and arr[k] not in temp:
            print(-1)
            index=-1
            break
        elif arr[k] in temp:
            if temp.index(arr[k])<index:
                index=temp.index(arr[k])
            temp.append(arr[k])
        else:
            temp.append(arr[k])
    if index!=-1:
        print(index+1)