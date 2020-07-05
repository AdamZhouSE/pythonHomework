n=int(input)
check=True
for i in range(2,n+1):
    if n%i==0 and (n!=2 or n!=3 or n!=5):
        check=False
        break
print(check)