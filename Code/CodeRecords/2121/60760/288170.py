n=int(input())
def func(n:int):
    if n>=0:
        count=0
        if n==0:
            count=0
        if n==1:
            count=10
        if n>=2:
           temp=9
           for i in range(n-1):
               temp=temp*(9-i)
           count=count+temp
        return count+func(n-1)
    return  0
print(func(n))