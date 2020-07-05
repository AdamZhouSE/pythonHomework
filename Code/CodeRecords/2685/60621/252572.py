a=eval(input())
for i in range(a):
    p=int(input())
    t=p
    s=""
    while p>10:
        s+="9"
        p-=9
    s=str(p)+s
    for i in range(t):
        s+="0"
    print(s)

