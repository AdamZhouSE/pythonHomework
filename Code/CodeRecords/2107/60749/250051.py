def power(num):
    k=findclosest(num)
    if num==pow(2,k):
        return True
    return False
    
def findclosest(num):
    k=0
    while num>=pow(2,k):
        if num<pow(2,k+1):
            return k
num=int(input())
print(power(num))