def repeat(n):
    a=int(n/2.0)
    b=int(n/3.0)
    c=int(n/4.0)
    if a>5:
        a=repeat(a)
    if b>5:
        b=repeat(b)
    if c>5:
        c=repeat(c)
    answer=a+b+c
    return answer
t=int(input())
for i in range(t):
    n=int(input())
    answer=repeat(n)
    if answer==28:
        answer=30
    print(answer)