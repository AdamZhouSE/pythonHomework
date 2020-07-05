num1=input()
num2=input()
num1=num1[1:-1].split(',')
num2=num2[1:-1].split(',')
num1=[int(x) for x in num1]
num2=[int(x) for x in num2]
cons=[]
other=[]
for i in range(len(num2)):
    am=num1.count(num2[i])
    for k in range(am):
        cons.append((num2[i]))
c = [x for x in num1 if x not in num2]
c.sort()
cons=[int(x) for x in cons]
print(cons+c)
