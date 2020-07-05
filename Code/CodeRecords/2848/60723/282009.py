temp=input().split()
nA=int(temp[0])
nB=int(temp[1])
temp=input().split()
k=int(temp[0])
m=int(temp[1])
temp=input().split()
arrayA=[]
for i in range(nA):
    arrayA.append(int(temp[i]))
temp=input().split()
arrayB=[]
for i in range(nB):
    arrayB.append(int(temp[i]))
flag=False
for i in range(nA-k):
    for j in range(nB-m):
        if max(arrayA[i:i+m])<min(arrayB[j:j+k]):
            flag=True
            break
if flag:
    print("YES")
else:
    print("NO")