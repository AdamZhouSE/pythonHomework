rb=input()
ar=list(map(int,input().split()))
res=0
for i in ar:
    res+=abs(i)
print(res)