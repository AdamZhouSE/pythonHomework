n=int(input())
m=n
num=input().split(' ')
count=0
sum1=int(0)
sum2=int(0)
for i in range(0,n):
    if int(num[m-1])>int(num[count]):
        if i%2==1:
            sum1=sum1+int(num[m-1])
        else:
            sum2=sum2+int(num[m-1])
        m=m-1
    else:
        if i%2==1:
            sum1=sum1+int(num[count])
        else:
            sum2=sum2+int(num[count])
        count=count+1
print(str(sum2)+" "+str(sum1))