def build(s,before):
    if before==subls:
        this[0]=this[0]+1
        return
    if len(s)==0:
        return
    for i in range(len(s)):
        a=s[i]
        sg=before+a
        k = len(sg)
        if sg==subls[:k]:
            build(s[i+1:],sg)

N=int(input())
result=[]
while N>0:
    nums=input().split(" ")
    n=int(nums[0])
    m=int(nums[1])
    s=input().split(" ")
    ls=s[0]
    subls=s[1]
    this=[0]
    ls=ls[ls.index(subls[0]):]
    i=0
    while i<len(ls)-1:
        if not subls.__contains__(ls[i]) and not subls.__contains__(ls[i+1]):
            ls=ls[:i]+ls[i+1:]
        else:
            i=i+1
    print(ls)
    first=[]
    for i in range(len(ls)):
        if ls[i]==subls[0]:
            first.append(i)
    for i in range(len(first)):
        j=first[i]
        build(ls[j+1:],ls[j])
    result.append(this[0])
    N=N-1

for i in range(len(result)):
    print(result[i])

