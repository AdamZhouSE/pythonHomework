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
        ans.append(str(li[l]))
        l-=1
        if r<l:
            ans.append(str(li[r]))
            r+=1
    print(" ".join(ans))