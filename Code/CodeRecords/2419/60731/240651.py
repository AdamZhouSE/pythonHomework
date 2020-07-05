num=input()
list=list(num)
num1=1
num2=0
for i in range(len(list)):
    num1*=int(list[i])
    num2+=int(list[i])
res=num1-num2
print(res)