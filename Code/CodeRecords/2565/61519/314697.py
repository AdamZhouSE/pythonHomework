num1=list(input().split(","))
num2=list(input().split(","))
for i in range(len(num1)):
    num1[i]=int(num1[i])
for i in range(len(num2)):
    num2[i]=int(num2[i])
num=num1+num2
n=int(len(num))
res=0
if n%2==0:
    res=((num[int(n/2)]+num[int((n/2)-1)])/2)
else:
    res=(num[(n-1)/2]/2)
print('%.5f' % res)