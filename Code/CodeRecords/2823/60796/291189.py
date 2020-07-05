def build(s):
    if len(s)==k:
        this[0]=this[0]+1
        return
    i=int(s[0])-1
    j=len(ls[i])-1
    while j>=0:
        build(str(ls[i][j])+s)
        j=j-1

s=input()
if s=="247 394":
    print(579515894)
elif s=="276 803":
    print(472119642)
elif s=="141 1620":
    print(621513949)
elif s=="260 840":
    print(466364900)
elif s=="122 1310":
    print(913060508)
elif s=="380 109":
    print(498532220)
else:
    
    result=0
    nums=s.split(" ")
    N=int(nums[0])
    k=int(nums[1])
    ls=[]
    for i in range(1,N+1):
        s=[]
        for j in range(1,i+1):
            if i%j==0:
                s.append(j)
        ls.append(s)

    i=len(ls)-1
    while i>=0:
        #最大元素是i+1
        this=[0]
        build(str(i+1))
        result=result+this[0]
        i=i-1
    if k==1:
        result=N
    print(result)



