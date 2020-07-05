n=int(input())
for p in range(n):
    a=int(input())
    aa=[0]
    bb=[0]
    for i in range(len(aa)):
        if aa[i]==a:
            a=bb[i]
            break
    print(a)