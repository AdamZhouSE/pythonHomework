A=[int(x) for x in input().split(',')]
key=int(input())
average=sum(A)/len(A)
B=[]
for i in A:
    if i>average:
        B.append(i-key)
    else:
        B.append(i+key)
print(max(B)-min(B))