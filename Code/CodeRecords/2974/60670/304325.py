def zhenghui(ss,typ):
    nn=len(ss)
    if nn%2==typ:# 0正回文 1非正回文
        return False
    else:
        l=0
        r=nn-1
        while l<r:
            if ss[l]!=ss[r]:
                return False
            else:
                l+=1
                r-=1
        return True

n=int(input())
s=input()
maxn=0
for t in range(1,n):
    left=s[0:t]
    right=s[t:]
    cntl=0
    cntr=0
    for i in range(0,len(left)):
        for j in range(1,len(left)+1):
            if zhenghui(left[i:j],0):
                cntl+=1
    for i in range(0,len(right)):
        for j in range(1,len(right)+1):
            if zhenghui(right[i:j],1):
                cntr+=1
    maxn=max(maxn,cntl*cntr)
print(maxn)