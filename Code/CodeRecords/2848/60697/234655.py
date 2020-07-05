size=list(map(int,input().split(' ')))
num=list(map(int,input().split(' ')))
A=list(map(int,input().split(' ')))
B=list(map(int,input().split(' ')))
k=num[0]
m=num[1]
sizeA=size[0]
sizeB=size[1]
a=A[k-1]
b=B[len(B)-m]
if(a<b):
    print("YES")
else:
    print("NO")