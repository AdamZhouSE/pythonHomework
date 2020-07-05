a=eval(input())
for i in range(0,a):
    count=0
    n=eval(input())
    temp=input().split(' ')
    b=map(eval,temp)
    list1=list(b)
    for i in range(0,n-1):
        for m in range(i+1,n):
            if(list1[i]>list1[m]):count+=1
    print(count)

