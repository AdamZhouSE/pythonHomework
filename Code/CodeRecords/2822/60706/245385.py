n=int(input())
so1=input().split(' ')
so2=input().split(' ')
num1=[]
for i in range(1,len(so1)):
    num1.append(int(so1[i]))
num2=[]
for i in range(1,len(so2)):
    num2.append(int(so2[i]))
temp=0
i=0
flag=0
while i<100:
    i=i+1
    if num1[0]>num2[0]:
        num1.append(num2[0])
        del(num2[0])
        temp=num1[0]
        del(num1[0])
        num1.append(temp)
    else:
        num2.append(num1[0])
        del(num1[0])
        temp=num2[0]
        del(num2[0])
        num2.append(temp)
    if len(num1)==0 and len(num2)==0:
        break
    if len(num1)==0:
        print(str(i)+' '+'2')
        flag=1
    if len(num2)==0:
        print(str(i)+' '+'1')
        flag=1
    if flag==1:
        break
if flag==0:
    print(-1)
    
        