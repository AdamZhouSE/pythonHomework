n=int(input())
def findgood(num):
    k=2
    while True:
        if judge(num,k):
            return k
        k+=1


def judge(num,k):
    temp=num*(k-1)+1
    exp=findcloset(temp, k)
    if temp==pow(k,exp):
        return True
    return False


def findcloset(num,k):
    i=0
    while num>=pow(k,i):
        if num<pow(k,i+1):
            return i
        i+=1
print(findgood(n))  