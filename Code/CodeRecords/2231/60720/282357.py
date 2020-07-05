size=int(input())
def isS(num):
    for i in range(2,num):
        if num%i==0:
            return False
    return True
for k in range(size):
    n=int(input())
    sum=0
    for i in range(2,n):
        if n%i==0 and isS(i):
            sum+=1
            n//=i
        if n==1:
            break
    if sum>=3 and n==1:
        print(1)
    else:
        print(0)