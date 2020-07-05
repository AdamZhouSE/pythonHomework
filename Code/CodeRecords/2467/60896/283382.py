a=eval(input())
for i in range(0,a):
    temp=input().split(' ')
    k=eval(temp[2])
    temp=input().split(' ')
    b=map(eval,temp)
    list1=list(b)
    temp=input().split(' ')
    b=map(eval,temp)
    list2=list(b)
    list1=list1+list2
    list1.sort()
    print(list1[k-1])