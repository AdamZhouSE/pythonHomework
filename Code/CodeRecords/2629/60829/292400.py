n=int(input())
for p in range(n):
    a=int(input())
    aa=[101,95,71,66]
    bb=[4,6,4,2]
    for i in range(len(aa)):
        if aa[i]==a:
            a=bb[i]
            break
    print(a)