t = int(input())
for _ in range(t):
    p=int(input())
    tm = int(input())
    r = int(input())
    result=p
    for _ in range(tm):
        result*=1+r/100
    print(int(p*r*tm/100))