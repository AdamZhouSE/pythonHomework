n=int(input())
ans=""
while n!=0:
    tmp=abs(n%(-2))
    ans+=str(tmp)
    n=(n-tmp)//(-2)
print("".join(reversed(ans)))