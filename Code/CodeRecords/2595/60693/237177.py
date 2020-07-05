cases=int(input())
for x in range(cases):
    n_k=input().split()
    n=int(n_k[0])
    k=int(n_k[1])
    print(pow(k,n-1))