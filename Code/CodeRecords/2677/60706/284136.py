t=int(input())
for i in range(t):
    n=int(input())
    list1=input().split(' ')
    count=0
    for i in range(n):
        for j in range(i+1,n):
            if int(list1[i])^int(list1[j])==0:
                count=count+1
    print(count)