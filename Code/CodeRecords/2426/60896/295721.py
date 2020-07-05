a=eval(input())
for i in range(0,a):
    n=eval(input())
    temp=input().split(' ')
    b=map(eval,temp)
    list1=list(b)
    list1.sort()
    print(list1[-1]*list1[-2]*list1[-3])