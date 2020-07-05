n=int(input())
m=int(input())
res=0
if n==1: res=2
elif n==2:
    if m==1:res=3
    else: res=4
elif n==3:
    if m==1: res=4
    else: res=8
print(res)