n=str(input())
l=list(n)
l.sort()
n=''.join(l)
nLen=len(n)
res=False
for i in range(32):
    numStr=str(int(pow(2,i)))
    if len(numStr)>nLen:
        break
    h=list(numStr)
    h.sort()
    numStr=''.join(h)
    if numStr==n:
        res=True
        break
if res:
    print('true')
else:
    print('false')