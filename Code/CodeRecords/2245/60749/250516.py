n=int(input())
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
        k+=1
def distance(n):
    if power(n):
        return 0
    if n==3:
        return 1
    res = ""
    while n > 0:
        res = str(n % 2) + res
        n = n // 2
    temp = []
    for h in res:
        temp.append(h)
    maxdistance = 0
    for x in range(0,len(temp)-1):
        if temp[x]=="1":


            for t in range(x+1,len(temp)):
                if temp[t]=="1":
                    maxdistance=max(maxdistance,t-x)
                    break
    return maxdistance
print(distance(n))