n=int(input())
num=1
while n>1:
    for x in range(n//2,0,-1):
        if n%x==0:
            n=n-x
            break
    num+=1
print(num%2==0)