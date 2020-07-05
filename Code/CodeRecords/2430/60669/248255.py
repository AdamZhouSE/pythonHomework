t=int(input())
for i in range(0,t):
    n=int(input())
    arr=list(map(int,input().split()))
    sum=int(input())
    result=[]
    for i in range(0,n):
        basis=arr[i]
        for j in range(i+1,n):
            behind=arr[j]
            if basis+behind==sum:
                result.append(str(basis)+" "+str(behind))
    if len(result)==0:
        print(-1)
    else:
        for item in result:
            print(item,end="")
            print(" "+str(sum))