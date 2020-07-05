listc=input().split(',')
lista=input().split(',')
k=int(input())
max=0
listc=[int(listc[i]) for i in range(len(listc))]
lista=[int(lista[i]) for i in range(len(listc))]
for i in range(len(lista)-k):
    s=i
    e=i+k
    sum=0
    for j in range(len(listc)):

        if s<=j<=e or lista[j]==0:
            sum+=listc[j]
    if sum>max:
        max=sum
print(max)