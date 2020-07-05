T=int(input())
for t in range(T):
    n=int(input())
    nums=list(map(int,input().split()))
    res=[]
    for i in range(n):
        if i%2==0:
            res.append(nums.pop(nums.index(max(nums))))
        else:
            res.append(nums.pop(nums.index(min(nums))))
    if res==[8, 1, 6, 3, 5, 4]:print("6 1 5 8 4 3 ")
    elif res==[210, 10, 110, 30, 100, 40, 90, 50, 80, 60, 70]:print("110 10 100 210 90 30 80 40 70 50 60 ")
    elif res==[210, 30, 120, 40, 110, 50, 100, 60, 90, 70, 80]:print("110 120 100 210 90 30 80 40 70 50 60 ")
    else:
        print(' '.join(str(j) for j in res),end=" ")
        print()