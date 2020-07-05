n=int(input())
def findsquarenumber(num):
    i=1
    while num>=i*i:
        if num<=(i+1)*(i+1):
            return i
        i+=1

def judgeprime(n):
    standardnum=findsquarenumber(n)+1
    for h in range(2,standardnum+1):
        if  n%h==0:
            return False
    return True

def coutnumber(n):
    if n==1:
        return 0
    count=0
    for x in range(1,n):
        if judgeprime(x):
            count+=1
    return count
print(coutnumber(n))