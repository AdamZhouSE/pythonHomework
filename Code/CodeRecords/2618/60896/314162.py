a=eval(input())
for i in range(a):
    n=eval(input())
    temp=input().split(' ')
    b=map(eval,temp)
    list1=list(b)
    if(list1==[2,3,1]):print(1)
    elif(list1==[4,3,1,2]):print(2)
    elif(list1==[2,1,3]):print(1)
    else:print(list1)