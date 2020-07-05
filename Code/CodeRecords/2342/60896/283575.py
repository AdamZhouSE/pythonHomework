a=eval(input())
for i in range(0,a):
    result=[]
    temp=input().split(' ')
    n=eval(temp[0])
    k=eval(temp[1])
    x=int (n/k)
    y=n%k
    temp=input().split(' ')
    b=map(eval,temp)
    list1=list(b)
    for m in range(0,x):
        temp=list1[k*m:k*m+k]
        temp.reverse()
        result+=temp
    temp=list1[x*k:n]
    temp.reverse()
    result+=temp
    for t in range(0,n):
        print(result[t],end=' ')
    print('')