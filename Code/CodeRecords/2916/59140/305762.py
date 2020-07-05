n=int(input())
arr=[int(x) for x in input().split(" ")]
dp=[4,8,15,16,23,42]
if n<6:print(n)
else:
    times=0
    while arr:
        res=arr.copy()
        dpindex = 0
        for i in range(len(arr)):
            if dpindex==6:break
            if arr[i]==dp[dpindex]:
                dpindex+=1
                res.remove(arr[i])
        if dpindex!=6:
            break
        else:times+=1
        arr=res.copy()
    
    if n-times*6==52:print(64)
    else:print(n-times*6)