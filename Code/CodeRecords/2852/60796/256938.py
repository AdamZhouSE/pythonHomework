n=int(input())
ls=input().split(" ")
ls=[int(x) for x in ls]
re=0
for i in range(n-1):
    this=0#这段寿司总长
    before=0#前半段长
    after=0#后半段长
    a=ls[i]
    if a==1:
        b=2
    else:
        b=1
    if ls[i+1:].__contains__(b):
        j=ls.index(b,i+1)
        before=j-i
    if j<n-1:
        if ls[j+1:].__contains__(a):
            k=ls.index(a,j+1)
            after=k-j
        else:
            after=n-j
    if before<=after:
        this=before*2
    else:
        this=after*2
    if this>re:
        re=this

print(re)

