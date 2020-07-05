#求素数
def getPrime(num):
    n=2
    li=[]
    while n>1:
        for i in range(2,n):
            if n%i==0:
                break
        else:
            if len(li)!=num:
                li.append(n)
            else:
                break
        n+=1
    return li[-1]

n=int(input())
for i in range(n):
    num=int(input())
    print(getPrime(num)**2 + 1)