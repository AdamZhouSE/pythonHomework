n=list(input())
n.sort()
judge=False
def pow2(n):
    res=1
    for i in range(n):
        res*=2
    return sorted(list(str(res)))
for j in range(20):
    if(n==pow2(j)):
        judge=True
        break
print(judge)
    