num=int(input())
data=input().split()
posNum=[]
negNum=[]
for i in range(num):
    if int(data[i])>=0:
        posNum.append(int(data[i]))
    else:
        negNum.append(int((data[i])))
num1=sum(posNum)
num2=sum(negNum)
print(num1-num2)