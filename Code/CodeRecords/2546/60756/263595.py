T=int(input())
Padovan=[1,1,1]
for t in range(T):
    n=int(input())
    while len(Padovan)<=n:
        Padovan.append(Padovan[-2]+Padovan[-3])
    print(Padovan[n])