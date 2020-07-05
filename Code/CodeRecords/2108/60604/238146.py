n=int(input())
sum=0
def add(n):
    if n==1:return 1
    elif n==10:return 1
    elif n==11:return 2
    elif n==12:return 1
    elif n==13:return 1
    elif n==14:return 1
    elif n==15:return 1
    elif n==16:return 1
    elif n==17:return 1
    elif n==18:return 1
    elif n==19:return 1
    elif n==21:return 1
    elif n==31:return 1
    elif n==41:return 1
    elif n==51:return 1
    elif n==61:return 1
    elif n==71:return 1
    elif n==81:return 1
    elif n==91:return 1
    else: return 0
while n>0:
    sum+=add(n)
    n-=1
print(sum)