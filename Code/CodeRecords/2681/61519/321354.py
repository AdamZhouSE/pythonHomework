n=int(input())
def com(k):
    if k==0:
        return 1
    if k%2==0:
        return com(k/2)+1
    if k%2==1:
        return com(k-1)+1
for i in range(n):
    k=int(input())
    ans=com(k)-1
    print(ans)