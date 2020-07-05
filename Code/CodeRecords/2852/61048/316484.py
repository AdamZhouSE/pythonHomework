def arr40():
    n=int(input())
    arr=[int(x) for x in input().split(' ')]
    res=0
    for i in range(n):
        cnt=1
        for j in range(i+1,n):
            if(arr[j]==arr[i]):
                cnt+=1
            else:
                break
        cnt_ex=1
        for j in range(i+cnt+1,n):
            if(arr[j]==arr[i+cnt] and cnt_ex<cnt):
                cnt_ex+=1
            else:break
        if(cnt_ex==cnt):
            res=max(cnt*2,res)
    print(res)
    return 

arr40()