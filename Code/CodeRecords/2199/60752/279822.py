def loop(depth,s):
    l=len(s)-1
    max=depth
    while l>0:
        sub=[]
        for ll in range(len(s)-l+1):
            ss=s[ll:ll+l]
            if sub.count(ss)==1:
                d=loop(depth+1,ss)
                if d>max:max=d
            sub.append(ss)
        l-=1
    return max

s=input()
print(loop(1,s))