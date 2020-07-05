p=int(input())
q=int(input())
res=0
if p%q==0:
    if p/q%2==0: res=2
    else: res=1
else:
    res=0
print(res)