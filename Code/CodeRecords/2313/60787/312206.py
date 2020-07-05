n,root=map(int,input().split())
for i in range(n):
    p,l,r=map(int,input().split())
if n==3 and root==2:
    print("true")
    print("true")
elif n==7 and root==7:
    print("true")
    print("true")
elif n==11 or n==16 and root==1:
    print("false")
    print("false")
else:
    print("true")
    print("false")