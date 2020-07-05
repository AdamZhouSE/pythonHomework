num=[]
num1=[]
for i in range(1,101):
    num.append(str(i))
    num1.append(str(i))
for i in range(len(num)):
    while len(num[i])<5:
        num[i]=num[i]+'0'
for i in range(len(num)):
    for j in range(i+1,len(num)):
        if int(num[i])>int(num[j]):
            num[i],num[j]=num[j],num[i]
            num1[i],num1[j]=num1[j],num1[i]
        elif int(num[i])==int(num[j]):
            if len(num1[i])>len(num1[j]):
                num1[i],num1[j]=num1[j],num1[i]
for s in range(len(num1)):
    print(num1[s])
