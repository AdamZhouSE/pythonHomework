t=int(input())
for i in range(t):
    n=int(input())
    list1=[]
    for j in range(n):
        list1.append(j+1)
    s=1
    while(s<=n):
        temp=1
        for j in range(s):
            temp=list1[0]
            del(list1[0])
            list1.append(temp)
        s=s+1
    print(list1)
            
        