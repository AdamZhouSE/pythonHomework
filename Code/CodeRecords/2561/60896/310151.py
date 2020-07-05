a=eval(input())
temp=input().split(' ')
n=eval(temp[0])
x=eval(temp[1])
for i in range(a):
    count=0
    list1=[]
    for i in range(n):
        temp=input().split(' ')
        b=map(eval,temp)
        list1+=list(b)
    list2=[]
    for i in range(n):
        temp=input().split(' ')
        b=map(eval,temp)
        list2+=list(b)
    for i in list1:
        for j in list2:
            if(i+j==x):
                count+=1
    print(count)
