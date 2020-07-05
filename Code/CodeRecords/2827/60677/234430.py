n=int(input())
lie=input().split()
lie=[int(x) for x in lie]
da=max(lie)
output=list(range(da))
for i in range(da):
    m=0
    for j in lie:
        if j>i:
            m+=1
    output[i]=m

output2=list(range(n))

for i in range(n):
    m=0
    for j in output:
        if j>i:
            m+=1
    output2[n-i-1]=m
output2=[str(x) for x in output2]
print(' '.join(output2))