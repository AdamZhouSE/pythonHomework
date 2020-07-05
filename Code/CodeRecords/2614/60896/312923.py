a=eval(input())
for i in range(a):
    n=eval(input())
    temp=input().split(' ')
    temp=map(eval,temp)
    list1=list(temp)
    temp=input().split(' ')
    temp=map(eval,temp)
    list2=list(temp)
    temp=input().split(' ')
    temp=map(eval,temp)
    list3=list(temp)
    count=0
    for i in range(n):
        for k in range(n):
            if(list1[i]==list2[i]+list3[k]):
                count+=1
    print(count)
