t=int(input())
for i in range(0,t):
    n=int(input())
    list1=input().split()
    list1=list(map(int,list1))
    count=0
    for j in range(0,n):
        for k in range(j+1,n):
            if(list1[k]<list1[j]):
                count=count+1
    print(count)