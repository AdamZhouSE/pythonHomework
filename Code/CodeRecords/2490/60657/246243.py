num1=input()
num1=num1[1:-1]
num1=num1.split(',')
num1=[int(i) for i in num1]
num2=input()
num2=num2[1:-1]
num2=num2.split(',')
num2=[int(i) for i in num2]
cons=[x for x in num1 if x in num2]
cons.sort()
print(cons)