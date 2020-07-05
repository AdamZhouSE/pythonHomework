def tree17():
    N=int(input())
    set=[]
    for i in range(N):
        set.append([int(x) for x in input().split(' ')])
    arr_len=max(max(set,key=lambda x:x[0])[0],max(set,key=lambda x:x[1])[1])
    arr=[0]*arr_len
    for order in set:
        for i in range(int(order[0])-1,int(order[1])-1):
            arr[i]=int(order[2])if(arr[i]<int(order[2])) else arr[i]
    res=sum(arr)
    print(res)
    return

tree17()