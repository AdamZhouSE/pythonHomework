def number(x):
    result=x*x*x+x   
    return result

t=int(input())
for i in range(t):
    n=int(input())
    print(number(n))