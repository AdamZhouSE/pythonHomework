a=eval(input())
for i in range(0,a):
    temp=input().split(' ')
    b=map(eval,temp)
    list1=list(b)
    len1=list1[0]
    len2=list1[1]
    temp=input().split(' ')
    b=map(eval,temp)
    list1=list(b)
    temp=input().split(' ')
    b=map(eval,temp)
    list2=list(b)
    judge=True
    for i in range(0,len2):
        if(list2[i] not in list1):
            judge=False
        else:
            list1.remove(list2[i])
    if(judge):
        print('Yes')
    else:
        print('No')