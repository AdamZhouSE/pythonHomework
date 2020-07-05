from collections import Counter
num=int(input())

def analyse(m):
    a=m//2
    b=m//3
    c=m//4
    if a+b+c<m:
        return m
    else:
        return analyse(a)+analyse(b)+analyse(c)


for i in range(num):
    m=int(input())
    result=analyse(m)
    print(result)