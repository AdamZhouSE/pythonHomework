a=eval(input())
for i in range(0,a):
    n=input()
    temp=input().split(' ')
    b=map(eval,temp)
    list1=list(b)
    temp=input().split(' ')
    b=map(eval,temp)
    list2=list(b)
    list1+=list2
    list1.sort()
    for t in range(0,len(list1)):
        print(list1[t],end=' ')
    print('')