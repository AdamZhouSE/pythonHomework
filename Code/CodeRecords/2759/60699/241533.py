cnt=int(input())
for i in range(0,cnt):
    list1=list(map(int,input().split(" ")))
    m=list1[0]
    n=list1[1]
    a=list1[2]
    b=list1[3]
    res=0
    for i in range(m,n+1):
        if i%a==0 or i%b==0:
            res+=1
    print(res)