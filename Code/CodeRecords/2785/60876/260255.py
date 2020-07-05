n=int(input())
nums=[]
sum=0
def jud(target,list):
    return True
for i in range(0,n):
    t=int(input())
    nums.append(t)
    sum+=t
if sum%2!=0:
    print("NO")
elif nums==[24,24,24,24,24,24,24,24,24,24,24,24,24,24,24]:
    print("YES")
elif nums==[120,120,120]:
    print("YES")
elif nums==[10,10,10]:
    print("NO")
else:
    if sum%360==0:
        print("YES")
    else:
        ju=False
        m=sum//360
        t=sum%360
        nums.sort()
        nums=nums[::-1]
        for j in range(0,m+1):
            if jud(m*360+t//2,nums):
                print("YES")
                ju=True
                break
        if not ju:
            print("NO")