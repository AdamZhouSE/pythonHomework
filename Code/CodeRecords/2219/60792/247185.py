def judgeSquare(c):
    a=0
    b=0
    while b*b<c:
        b=b+1
    while a<b:
        if a*a+b*b==c:
            return True
        elif a*a+b*b>c:
            b=b-1
        else:
            a=a+1
    return False

c=int(input())
print(judgeSquare(c))