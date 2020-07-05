import decimal
def right(n):
    if n==1:
        return 1.0
    return 0.5

def accurate(n):
    n=round(n,5)
    n=str(n)
    if len(n)==3:
        n=n+'0000'
        return n
    elif len(n)==7:
        print(n)
        return n
    else:
        print(n)
        for i in range(7-len(n)):
            n=n+'0'
        return n
n=int(input())
answer=float(right(n))
answer=accurate(answer)
print(answer)