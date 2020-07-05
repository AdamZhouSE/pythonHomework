K=int(input())
def f(n):
    cnt=0
    while(n!=0):
        cnt=cnt+int(n/5)
        n=int(n/5)
    return cnt
base=4*K
result=0
while(True):
    T=f(base)
    if(T==K):
        result=5
        break
    elif(T>K):
        result=0
        break
    base=base+5
print(result)