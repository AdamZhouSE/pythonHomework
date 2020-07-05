def shuzu(a,b1,b2):
    b1.sort(reverse=True)
    b2.sort(reverse=True)
    ans=0
    i=0
    j=0
    while a[0]>0:
        if b1[i]>=b2[j]:
            if a[1]-i>0:
                ans=ans+b1[i]
                i=i+1
            else:
                ans=ans+b2[j]
                j=j+1
        else:
            if a[2]-j>0:
                ans=ans+b2[j]
                j=j+1
            else:
                ans=ans+b1[i]
                i=i+1
        a[0]=a[0]-1
    return ans
count=int(input())
for i in range(0,count):
    a=input().split()
    b1=input().split()
    b2=input().split()
    a=[int(x) for x in a]
    b1=[int(x) for x in b1]
    b2=[int(x) for x in b2]
    print(shuzu(a,b1,b2))