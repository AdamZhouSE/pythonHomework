num=list(map(int,input().strip().split()))
l=len(num)
num1=list[]
for i in range(1,l):
    num1.append(list[l-i])
for i in range(l-1):
    print(num1[i],end=" ")