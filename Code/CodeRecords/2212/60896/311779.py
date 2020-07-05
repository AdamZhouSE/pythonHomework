a=int(input())
for i in range(a):
    list1=[]
    b=int(input())
    for i in range(1,b+1):
        if(b%i==0):list1.append(i)
    count=0
    for i in list1:
        count+=i
    if(count<2*b):print(1)
    else:print(0)