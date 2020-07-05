length=int(input())
give=input().split()
res=0
for n in give:
    if int(n)>=0:
        res+=int(n)
    else:
        res -= int(n)
print(res)