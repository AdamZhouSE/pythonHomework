list=input()
num0=list.count('0')
num1=list.count('1')
num2=list.count('2')
result=[]
for i in range(0, num0):
    result.append(0)
for i in range(0, num1):
    result.append(1)
for i in range(0, num2):
    result.append(2)
print(result)