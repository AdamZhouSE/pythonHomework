def money(p,tm,r):
    answer=int(p*tm*r/100)
    return answer

t=int(input())
for i in range(t):
    p=int(input())
    tm=int(input())
    r=int(input())
    answer=money(p,tm,r)
    print(answer)