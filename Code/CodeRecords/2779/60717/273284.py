n=int(input())
for i in range(0,n):
    m=int(input())
    list1=input().split()
    for j in range(0,m):
        list1[j]=int(list1[j])
    a=min(list1)
    b=max(list1)
    count=1
    while True:
        if a*count%b==0:
            print(a*count)
            break
        else:
            count+=1