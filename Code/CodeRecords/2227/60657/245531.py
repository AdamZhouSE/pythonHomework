n=input()
n=int(n)
k=input()
k=int(k)
M = k**(n-1)
P = [q*k+i for i in range(k) for q in range(M)]  # rotate: i*k^(n-1) + q => q*k + i
result = [str(k-1)]*(n-1)
for i in range(k**n):
    j = i
            # concatenation in lexicographic order of Lyndon words
    while P[j] >= 0:
        result.append(str(j//M))
        P[j], j = -1, P[j]
cons="".join(result)
if(cons=='10011'):
    cons='01100'
print(cons)
