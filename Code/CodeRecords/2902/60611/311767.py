num=int(input())
n=num//2
for i in range(num):
    s=""
    a=0
    if i<=n:
        a=n-i
    else:
        a=i-n
    for j in range(a):
        s+="*"
    for j in range(num-2*a):
        s+="D"
    for j in range(a):
        s+="*"
    print(s)