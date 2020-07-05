num=[0for i in range(5)]
count=0
for i in range(5):
    num[i]=input()
num1=[0for i in range(5)]
for i in range(5):
    num1[i]=num[i].split(" ")
for i in range(5):
    if num1[i]!=['0', '0', '0', '0', '0']:
        num=num1[i]
        if i==0 or i==4:
            count = count+2
        elif i==1 or i==3:
            count = count + 1
        break
for i in range(5):
    if num[i]=='1':
        if i==0 or i==4: count=count+2
        elif i==1 or i==3: count = count +1
        break
print(count)