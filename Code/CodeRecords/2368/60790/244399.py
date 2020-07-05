t=int(input())
for i in range(0,t):
    n=int(input())
    list1=input().split()
    list1=list(map(int,list1))
    list1.sort(reverse=True)
    list2=[0]*n
    if(n%2==0):
        for j in range(0,int(n/2)):
            list2[2*j]=list1[0]
            list2[2*j+1]=list1[-1]
            del list1[0]
            del list1[-1]
    else:
        for j in range(0,int(n/2)):
            list2[2*j]=list1[0]
            list2[2*j+1]=list1[-1]
            del list1[0]
            del list1[-1]
        list2[-1]=list1[0]
    print(*list2)