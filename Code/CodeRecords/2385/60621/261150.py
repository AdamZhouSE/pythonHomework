a=eval(input())
for i in range(a):
    num = eval(input())
    if num%2==1:
        k=num//2
        ans=2**(k+1)+2**(k)-1
    else:
        k=num//2
        ans=2**(k+1)-1
    print(ans)