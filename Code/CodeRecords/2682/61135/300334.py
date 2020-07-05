def toStr(n, base):
    mid="0123456789ABCDEF"
    if n<base:
        return mid[n]
    else:
        return toStr(n//base, base)+mid[n%base]
nums=int(input())
res=[]
for i in range(nums):
    num=input().split(" ")
    num=list(int(x) for x in num)
    l=num[1]-1
    r=num[2]
    twostrtarg=list(toStr(num[0],2))
    twostrtarg.reverse()
    tempstr="".join(twostrtarg[l:r])
    templists=twostrtarg[0:l]
    templists.extend(twostrtarg[r:])
    tempstr=tempstr.replace("0","1")
    templists.insert(l,tempstr)
    templists.reverse()
    mid=int("".join(templists),2)
    res.append(mid)
for i in res:
    print(i)