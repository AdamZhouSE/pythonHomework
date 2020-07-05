a=eval(input())
temp=input().split(',')
b=map(eval,temp)
list1=list(b)
n=1
count=0
while(True):
    num=n
    for i in range(0,len(list1)):
        while(num%list1[i]==0):
            num/=list1[i]
    if(num==1):
        count+=1
    if(count==a):
        print(n)
        break
    n+=1
