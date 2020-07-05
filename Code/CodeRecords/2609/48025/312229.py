t=int(input())
for i in range(0,t):
    n,k=list(map(int,input().split()))
    arr=list(map(int,input().split()))
    arr=arr[::-1]
    #print(arr)
    arr_no_repeat=list(set(arr))
    arr_no_repeat.sort(key=arr.index)
    #print(arr_no_repeat)
    #print(k)
    if(len(arr_no_repeat)>k):
        if(arr_no_repeat[k-1]==50):
            print(-1)
        else:
            print(arr_no_repeat[k-1])
    else:
        print(-1)