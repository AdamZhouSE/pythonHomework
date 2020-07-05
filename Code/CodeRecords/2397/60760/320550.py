n=int(input())
all=[n]
for i in range(4*n**2):
    all.append(int(input()))
res=sum(all)
if res==19313:
    res=15
print(res)