import sys
a=int(input())
s=sys.stdin.read()
sli=s.split("\n")
for i in range(a):
    s=sli[2*i]
    t=sli[2*i+1]
    slist=list(s)
    tlist=list(t)
    n=len(s)
    res=[]
    minwindow=n+1
    if len(t)==1 and tlist[0]==slist[-1]:
        print(t)
    else:
        for k in range(n-1):
            if k==4:
                debug=1
            for j in range(k+1,n+1):
                ans=slist[k:j]
                isvalid=1
                for ch in t:
                    if ch not in ans:
                        isvalid=0
                        break
                if isvalid==1:
                    if len(ans)<minwindow:
                        minwindow=len(ans)
                        if len(res)!=0:
                            del(res[0])
                        res.append(ans)
        if len(res)==0:
            print(-1)
        else:
            out="".join(res[0])
            print(out)