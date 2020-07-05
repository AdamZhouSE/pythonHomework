a=int(input())
b=int(input())
#print(a)
#print(b)

ans = 0

while b>a:
    ans=ans+1
    if b%2==1:
        b=b+1
    else:
        b=b/2
print(int(ans+a-b))
        