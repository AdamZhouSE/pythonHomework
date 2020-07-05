T=int(input())
for t in range(T):
    n=int(input())
    padovan=[1,1,1]
    if n>=2:
        for i in range(n-2):
            padovan.append(padovan[len(padovan)-3]+padovan[len(padovan)-2])
    print(padovan[n])
