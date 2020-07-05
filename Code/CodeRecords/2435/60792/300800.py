n,m=map(int,input().split())
list1=[]
for i in range(0,n):
    list1.append(input())
for i in range(0,m):
    start,end=map(int,input().split())
    list2=[]
    for j in range(start-1,end):
        list2.append(list1[j])
    list2.sort()
    print(list2[-1])