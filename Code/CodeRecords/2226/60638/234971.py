def divide(n):
    number=n
    exp=10
    while True:
        if n==0:
            break
        num=n%exp
        if num==0:
            return False
        if number%num!=0:
            return False
        n=(n-num)/exp
    return True

low=int(input())
up=int(input())
numbers=range(low,up+1)
res=[]
for number in numbers:
    if divide(number)==True:
        res.append(number)
print(res)