def get_maxsum(n):
    p1=n//2
    p2=n//3
    p3=n//4
    if p1+p2+p3>n:return get_maxsum(p1)+get_maxsum(p2)+get_maxsum(p3)
    else:return n

cases=int(input())
for i in range(cases):
    n=int(input())
    print(get_maxsum(n))