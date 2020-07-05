import sys
a=int(input())
s=sys.stdin.read()
sli=s.split("\n")
for i in range(a):
    s=sli[2*i]
    t=sli[2*i+1]
    n=len(s)
    isUsed=[0]*n
    ans=[]
    minwindow=n
    findsubstr(isUsed,s,0,ans,minwindow)