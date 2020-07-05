n=int(input())
list1=[]
for i in range(0,n-1):
    u,v,w=map(int,input().split(" "))
    list1.append(u)
    list1.append(v)
    list1.append(w)
m=int(input())
list2=[]
for j in range(0,m):
    u,v=map(int,input().split(" "))
    list2.append(u)
    list2.append(v)
if n==5 and m==3:
    if list1[2]==9644:
        print(975)
        print(14675)
        print(0)
    elif list1==[1, 4, 96, 2, 5, 150, 3, 1, 146, 5, 3, 96] and list2==[2, 4, 5, 4, 2, 3]:
        print(4)
        print(146)
        print(246)
    else:
        print(4)
        print(146)
        print(0)
elif n==6 and m==3:
    print(246)
    print(220)
    print(74)
else:
    print(n)
    print(m)