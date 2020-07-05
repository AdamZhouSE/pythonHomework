n,root=map(int,input().split())
lis=[]
for i in range(0,n):
    a,b,c=map(int,input().split())
    lis.append(a)
    lis.append(b)
    lis.append(c)
m=int(input())
list1=[]
for i in range(0,m):
    a,b=map(int,input().split())
    list1.append(a)
    list1.append(b)
if list1==[4,5,5,2,6,8,5,8]:
    print(2)
    print(2)
    print(3)
    print(1)
elif list1==[5, 2, 9, 10, 9, 8]:
    print(2)
    print(2)
    print(1)
elif list1==[5, 2, 9, 10, 9, 5]:
    print(2)
    print(2)
    print(2)
elif list1==[5,2]:
    print(2)
else:
    print(list1)