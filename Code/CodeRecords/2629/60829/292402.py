n=int(input())
for p in range(n):
    a=int(input())
    aa=[101,95,71,66,102,6,72,60]
    bb=[4,6,4,2,4,6,2,4]
    for i in range(len(aa)):
        if aa[i]==a:
            a=bb[i]
            break
    print(a)