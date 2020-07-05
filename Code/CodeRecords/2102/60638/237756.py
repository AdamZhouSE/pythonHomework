def isPara(n):
    for i in range(2,n):
        if n%i==0:
            return False
    return True
num=int(input())
count=0
for i in range(2,num+1):
    if isPara(i):
        count=count+1
print(count)