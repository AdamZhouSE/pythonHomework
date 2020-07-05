n=int(input())
heighth=[]
judge=True
for i in range(n):
    tmp=input().split(" ")
    a=int(tmp[0])
    b=int(tmp[1])
    if len(heighth)==0:
        heighth.append(max(a,b))
    else:
        if min(a,b)>heighth[-1]:
            print("NO")
            judge=False
            break
        elif max(a,b)<=heighth[-1]:
            heighth.append(max(a,b))
        else:
            heighth.append(min(a,b))
if judge==True:
    print("YES")