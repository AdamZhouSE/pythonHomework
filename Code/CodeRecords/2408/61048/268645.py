def numop9():
    num=int(input())
    primeCount=0
    for i in range(1,num+1):
        if isprime(i):
            primeCount+=1

    res=factorial(primeCount)*factorial((num-primeCount))
    res=res%(1000000000+7)
    print(res)
    return



def isprime(num):
    res=True
    if num==1 or num==0:
        res=False
    elif num==2 or num==3:
        res=True
    else:
        for i in range(2,num):
            if(num%i==0):
                res=False
                break
    return res

def factorial(num):
    res=1
    for i in range(1,num+1):
        res=res*i
    return res

numop9()