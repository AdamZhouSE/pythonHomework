def check(maxN,numbers,n):
    itr=0
    while(n>0):
        sum=0
        while(itr<len(numbers)):
            sum=sum+numbers[itr]
            if sum>maxN:
                break
            itr=itr+1
        n=n-1
    if(itr==len(numbers)):
        return True
    else:
        return False
inpu=input()[1:-1]
numbers=list(map(int,inpu.split(",")))
n=int(input())
maxN=max(numbers)
while(True):
    if(check(maxN,numbers,n)):
        break
    maxN=maxN+1
print(maxN)