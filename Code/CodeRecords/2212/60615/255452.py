count=int(input())

list2=[]

while count>0:  #count sub
    sum=0
    list1 = []
    num=int(input())
    i=1
    while i**2<=num:
        if num%i==0:
            list1.append(i)
            list1.append(num/i)
        i=i+1
    list1=list(set(list1))
    for i in list1:
        sum=sum+i
    if sum<num*2:
        list2.append(1)
    else:
        list2.append(0)
    count=count-1
for i in list2:
    print(i)