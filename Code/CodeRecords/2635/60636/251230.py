def f(x):
    count_2=0
    count_5=0
    for i in range(1,x+1):
        a=i
        while(a%2==0):
            a=a/2
            count_2=count_2+1
        b=i
        while(b%5==0):
            b=b/5
            count_5=count_5+1
    return min(count_2,count_5)
res=[]
k=int(input())
i=0
while(True):
    if(f(i)==k):
        print(res)
    elif(f(i)>k):
        break
    i=i+1
print(len(res))