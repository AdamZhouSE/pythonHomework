def func(list1):
    sum1=sum(list1)
    s=int(sum1/3)
    t1=0
    t2=0
    it=0
    while(t1<s):
        t1=t1+list1[it]
        it=it+1
    if(t1!=s):
        return True
    else:
        while(t2<s):
            t2=t2+list1[it]
            it=it+1
        if(t2!=s):
            return True
        else:
            return False
n=int(input())
list1=input().split()
list1=list(map(int,list1))
sum1=sum(list1)
count=0
if(sum1%3!=0):
    print(0)
elif(func(list1)):
    print(0)
else:
    for i in list1:
        if(i==0):
            count=count+1
    print(count+1)
    
    