def getNum(n):
    result=0
    while n>0:
        result=result+(n%10)*(n%10)
        n=n//10
    return result

def isHappyNum(n):
    temp=n
    while(True):
        temp=getNum(temp)
        if(temp==89):
            return False
        elif temp==1:
            return True
    
def min_happynum(n):
    n=n+1
    while(not(isHappyNum(n))):
        n=n+1
    return n    

num=int(input())
for i in range(0,num):
    n=int(input())
    print(min_happynum(n))