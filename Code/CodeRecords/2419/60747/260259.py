n=input()
num=[]
sum=0
mul=1
for i in range(len(n)):
    num.append(int(n[i]))
    sum=sum+num[i]
    mul=mul*num[i]
print(mul-sum)
