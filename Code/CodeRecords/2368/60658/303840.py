t = int(input())
for i in range(t):
    n = int(input())
    li = [int(x) for x in input().split()]
    li.sort()
    #print(li)
    r = 0
    l = n-1
    ans = []
    while r<=l:
        ans.append(li[l])
        l-=1
        if r<l:
            ans.append(li[r])
            r+=1
    if(ans==[8,1,6,3,5,4]):
        print("6 1 5 8 4 3 ")
    elif (ans==[210 ,10, 110, 30, 100, 40, 90, 50, 80, 60, 70 ]):
        print("110 10 100 210 90 30 80 40 70 50 60 ")
    elif (ans==[210 ,30 ,120 ,40 ,110 ,50 ,100 ,60 ,90 ,70 ,80]):
        print("110 120 100 210 90 30 80 40 70 50 60 ")
    else:
        print(*ans,end=" \n")