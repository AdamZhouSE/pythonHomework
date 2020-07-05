def Iteration(arr,n):
    if(len(arr)==1):
        return arr[0]
    else:
        new_arr=[]
        if(n==0):
            for i in range(0,len(arr),2):
                new_arr.append(arr[i]|arr[i+1])
        else:
            for i in range(0,len(arr),2):
                new_arr.append(arr[i]^arr[i+1])
        return Iteration(new_arr,1-n)
n,m=map(int,input().split(' '))
arr=list(map(int,input().split(' ')))
query=[]
for i in range(m):
    query.append(list(map(int,input().split(' '))))
for i in query:
    temp=arr[i[0]-1]
    arr[i[0]-1]=i[1]
    print(Iteration(arr,0))

