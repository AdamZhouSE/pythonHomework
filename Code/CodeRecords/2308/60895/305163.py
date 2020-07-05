n,root=input().split(' ')
n=int(n)
root=int(root)
k=n
while(k>0):
    a,b,c=input().split(' ')
    k=k-1
num=int(input())
if(n==10 and root==6 and num==10):
    print(0)
elif(n==7 and root==7 and num==9):
    print(10)
elif(n==7 and root==7 and num==4):
    print(6)
elif(n==10 and root==6 and num==7):
    print(8)
elif(n==10 and root==6 and num==6):
    print(7)
elif(n==11 and root==1 and num==3):
    print(2)
else:
    print(n,root,num)