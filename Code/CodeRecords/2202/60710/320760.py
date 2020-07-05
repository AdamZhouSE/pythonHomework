T=int(input())

for i in range(0,T):
    L=int(input())

    f0=0
    f1=1
    f2=0

    for j in range(0,L):
        f2=f1+f0
        f0=f1
        f1=f2

    print(f2)

