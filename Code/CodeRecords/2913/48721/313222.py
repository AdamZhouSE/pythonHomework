ins=int(input())
l=[]
m=0
b=input().split()
for i in range(ins):
    m=m+int(b[i])
if m%2==0:
    print("YES")
else:
    print("NO")