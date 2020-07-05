t=int(input())
def prime_li(num):
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

while t:
    num=int(input())
    print (1+(prime_li(num))**2)
    t-=1