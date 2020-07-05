arr=list(input())
sign=True
LR=True
dicX={'x':0}
ans=0
num=""
for i in arr:
    L=len(num)
    Y=sign^LR
    if i=='-':
        sign=False
    elif i=='+':
        sign=True
    elif i=='x':
        if not Y:
            dicX['x']+=(int(num) if num!="" else 1)
            num=""
        else:
            dicX['x']-=(int(num) if num!="" else 1)
            num=""
    elif i == '=':
        sign = True
        LR = False
    else:
        num+=i
    if len(num)==L and L:
        if not Y:
            ans-=int(num)
        else:
            ans+=int(num)
        num=""
if num!="":
    if not sign^LR:
        ans -= int(num)
    else:
        ans += int(num)
if dicX['x']==0:
    print("Infinite solutions" if ans==0 else "No solution")
else:
    print("x=%d" %(ans//dicX['x']))