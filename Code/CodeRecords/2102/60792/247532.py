def isSuShu(n):
    if(n==2):
        return True
    if n==1:
        return False
    else:
        for i in range(2,n):
            if n%i==0:
                return False
        return True
    
n=int(input())
count=0
for i in range(1,n):
    if(isSuShu(i)):
        count=count+1
print(count)