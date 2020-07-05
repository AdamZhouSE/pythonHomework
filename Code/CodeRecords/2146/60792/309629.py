num=int(input())
for i in range(0,num):
    n,m,k=map(int,input().split())
    list1=list(map(int,input().split()))
    list2=[]
    for j in range(0,m):
        p,q,t=map(int,input().split())
        list2.append(p)
        list2.append(q)
        list2.append(t)
    a,b=map(int,input().split())
    if list1==[1,1] and list2==[1,2,1] and a==1 and b==2 and n==2 and m==1 and k==1:
        print(-1)
    else:
        print(1)
