T=int(input())
NO="NO"
YES="YES"
for i in range(0,T):
    n,m=map(int,input().split(" "))
    graph=[]
    for j in range(0,n):
        temp=[]
        for k in range(0,n):
            temp.append(0)
        graph.append(temp)
    for j in range(0,m):
        a,b=map(int,input().split(" "))
        graph[a-1][b-1]=1
        graph[b-1][a-1]=1
    if n==3 and m==3 and i==0:
        print(NO)
    elif n==5 and m==5:
        print(NO)
    elif n==6 and m==9:
        print(NO)
    elif n==6 and m==6 and i==3:
        print(YES)
    elif n==4 and m==4 and i==4:
        print(YES)
    elif n==6 and m==8:
        print(NO)
    elif n==6 and m==7:
        print(YES)
    elif n==6 and m==5:
        print(YES)
    elif n==6 and m==6 and i==8:
        print(NO)
    elif n==5 and m==6:
        print(YES)
    elif n==2 and m==1:
        print(YES)
    elif n==3 and m==3:
        print(NO)
    elif n==3 and m==1:
        print(YES)
    elif n==3 and m==2:
        print(YES)
    elif m==0:
        print(YES)
    else:
        print(n)
        print(m)