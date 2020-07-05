n=int(input())
for i in range(n):
    m=int(input())
    s=input()
    r=0
    for j in s:
        if j!=' ':
            r+=int(j)
    if r%3==0:
        print(1)
    else:
        print(0)