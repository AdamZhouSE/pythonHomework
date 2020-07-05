n=int(input())
check=True
for i in range(2,n+1):
    if n%i==0 and i!=2 and i!=3 and i!=5:
        check=False
        break
print(check)