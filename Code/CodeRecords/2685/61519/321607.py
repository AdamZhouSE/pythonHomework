n=int(input())
def com(k):
    if k>10:
        return com(k-9)+'9'
    if k<10:
        return str(k)
for i in range(n):
    k=int(input())
    a=0
    b=0
    res=""
    if k>10:
        res=com(k)
    else:
        res=str(k)
    for i in range(k):
        res=res+'0'
    print(int(res))