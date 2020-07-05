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
    subl=[]
    subr=[]
    cntl=0
    cntr=0
    for i in range(0,len(left)):
        for j in range(1,len(left)+1):
            tmp=left[i:j]
            if zhenghui(tmp,0) and (not tmp in subl):
                subl.append(tmp)
                cntl+=1
    for i in range(0,len(right)):
        for j in range(1,len(right)+1):
            tmp=right[i:j]
            if ( zhenghui(tmp,1)) and (not tmp in subr):
                cntr+=1
                subr.append(tmp)
    maxn=max(maxn,cntl*cntr)
print(maxn)