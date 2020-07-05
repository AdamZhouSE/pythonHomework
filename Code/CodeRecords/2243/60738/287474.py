p=int(input())
q=int(input())
def mirror(p,q):
    while(p%2==0 and q%2==0):
        p/=2
        q/=2
    return 1-p%2+q%2
print(mirror(p,q))