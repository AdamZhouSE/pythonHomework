import re
T=int(input())
for i in range(T):
    n=int(input())
    nums=list(map(int,re.sub("\D"," ",input()).split()))
    a,b,c,d=-1,0,0,0
    check=False
    for i in range(n-3):
        if check:
            break
        for j in range(i+1,n):
            if check:
                break
            s=nums[i]+nums[j]
            for k in range(i+1,n):
                if check:
                    break
                if k==i or k==j:
                    continue
                for l in range(k+1,n):
                    if l==i or l==j:
                        continue
                    elif s==nums[k]+nums[l]:
                        a,b,c,d=i,j,k,l
                        check=True
                        break
    if a==-1:
        print("no pairs")
    else:
        print("%d %d %d %d" % (a, b, c, d))