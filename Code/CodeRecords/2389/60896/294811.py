a=eval(input())
for i in range(0,a):
    n=eval(input())
    temp=input().split(' ')
    b=map(eval,temp)
    list1=list(b)
    list1.sort()
    len1=int(len(list1)/2)
    for i in range(0,len1):
        temp=list1[2*i]
        list1[2*i]=list1[2*i+1]
        list1[2*i+1]=temp
    for i in range(0,len(list1)-1):
        print(list1[i],end=' ')
    print(list1[-1])