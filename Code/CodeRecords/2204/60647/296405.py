a=int(input())
b=int(input())
def pr(a,b):
    if b>a:
        print(a,end=" ")
        return pr(a+1,b)
    elif b==a:
        print(a)
        return pr(a + 1, b)
    else:
        print(' ')
        return 0
pr(a,b)