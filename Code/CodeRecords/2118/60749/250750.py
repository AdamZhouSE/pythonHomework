def power(num):
    k=findclosest(num)
    if num==pow(3,k):
        return True
    return False

def findclosest(num):
    k=0
    while num>=pow(3,k):
        if num<pow(3,k+1):
            return k
        k+=1
num=int(input())
if num==0:
    print(False)
else:
    
    print(power(num))

