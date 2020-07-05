a=input()
a=int(a)
cons=[]
for i in range(1,a-1):
    if a%i==0:
        cons.append(i)
if sum(cons)==a:
    cons='True'
else:
    cons='False'
print(cons)
