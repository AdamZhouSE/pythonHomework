n=int(input())
x=[int(n) for n in input().split()]
nodd=0
nnodd=0
for i in range(0,n):
    if x[i]%2==0:
        nnodd+=1
    else:
        nodd+=1
if nnodd>nodd:
    print(nodd)
else:
    print(nnodd)