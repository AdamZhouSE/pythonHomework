def shakeHands(n):
    if n==0 or n==1:
        return 1
    else:
        res=0
        for i in range(0,n):
            res=res+shakeHands(i)*shakeHands(n-1-i)
        return res

T=int(input())

for k in range(0,T):
    num=int(input())
    print(shakeHands(round(num/2)))