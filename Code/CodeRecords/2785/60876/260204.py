n=int(input())
nums=[]
sum=0
def jud(target,list):
    start=0
    end=len(list)
    if sum%360==0:
        return True
    for j in range(start,end):
        if list[j]==target:
            return True
    for j in range(start,end):
        temp=list[start:end]
        del temp[j]
        length=len(temp)
        if jud(target-list[j],temp):
            return True
    return False
for i in range(0,n):
    t=int(input())
    nums.append(t)
    sum+=t
if sum%2!=0:
    print("NO")
else:
    if sum%360==0:
        print("YES")
    else:
        ju=False
        m=sum//360
        t=sum%360
        for j in range(0,m+1):
            if jud(m*360+t//2,nums):
                print("YES")
                ju=True
                break
        if not ju:
            print("NO")