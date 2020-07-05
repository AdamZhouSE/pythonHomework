l=input().split(" ")
m=int(l[0])
n=int(l[1])
a=input()
b=input()
k=0
index=[]
for i in range(n-m+1):
    isFit=True
    for j in range(m):
        if a[j]=="*" or b[i+j]=="*":
            continue
        elif a[j]!=b[i+j]:
            isFit=False
            break
    if isFit:
        k+=1
        index.append(i)
print(k)
for i in range(len(index)):
    print(index[i]+1,end=" ")
print()