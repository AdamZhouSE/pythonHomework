num=int(input())
for i in range(0,num):
    n=int(input())
    list1=list(map(int,input().split(" ")))
    k=int(input())
    count=0
    for j in range(0,n):
        for m in range(j+1,n):
            if list1[j]+list1[m]==k:
                print(list1[j],end=" ")
                print(list1[m],end=" ")
                print(k)
                count+=1
    if count==0:
        print("-1")