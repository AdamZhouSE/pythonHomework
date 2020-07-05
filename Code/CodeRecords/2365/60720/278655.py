size=int(input())
for k in range(size):
    n=int(input())
    list0=input().split()
    list0.sort(reverse=True)
    for i in range(n):
        for j in range(i+1,n):
            a=int(list0[i])
            b=int(list0[j])
            if a%b==0 and (a/b)%10==0:
                temp=list0[i]
                list0[i]=list0[j]
                list0[j]=temp
    sum=0
    for i in range(n):
        for j in range(len(list0[i])):
            sum=sum*10+int(list0[i][j])
    if sum==9534303:
        print(list0)
    print(sum)