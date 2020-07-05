a=eval(input())    
for i in range(0,a):
    temp=input().split(' ')
    b=map(eval,temp)
    list1=list(b)
    n=list1[0]
    k=list1[1]
    temp=input().split(' ')
    b=map(eval,temp)
    list1=list(b)
    list1.sort()
    for m in range(n-1,n-k-1,-1):
        print(list1[m],end=' ')
    print('')