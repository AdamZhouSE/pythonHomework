line=input().split(',')
num=list(map(int, line))
val=int(input())
length=len(num)
res=[]

if val<num[0] or val>num[-1] or (not (val in num)):
    res.append(-1)
    res.append(-1)
    print(res)
else:
    ind=num.index(val)
    res.append(ind)
    while ind<length and num[ind]==val:
        ind=ind+1
    res.append(ind-1)
    print(res)

    