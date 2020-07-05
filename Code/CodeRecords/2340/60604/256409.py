n=int(input())
def findl(a):
    for i in range(1,len(a)):
        if a[i]<=a[i-1]:
            return i-1
def findr(a):
    for i in range(len(a)-2,-1,-1):
        if a[i]<=a[i+1]:
            return i+1
for i in range(n):
    size=int(input())
    a=input().split()
    for j in range(size):
        a[j]=int(a[j])
    #print(a)
    left=findl(a)
    right=findr(a)
    #print(left)
    #print(right)
    if (a[left]>=a[right]):
        b=a[right]
    else:
        b=a[left]
    res=0
    if right-left>1:
        for j in range(left+1,right):
            if a[j]<b:
                res+=b-a[j]
    print(res)

















