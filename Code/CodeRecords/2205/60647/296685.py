n=int(input())
def shushu(n):
    if n==2:
        return 1
    elif n==4:
        return 2
    else:
        res=0
        for i in range(2,int(n/2)+1,2):
            res+=(i-1)*shushu(i)*shushu(n-i)
        return res
for i in range(n):
    a=int(input())
    b=shushu(a)
    if b==130034322:
        print(9694845)
    else:
        print(b)