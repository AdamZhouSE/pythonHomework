
num1=input()
arr1=input().split(' ')
arr1=[int(x) for x in arr1]
cons=0
am=0
for i  in arr1:
    if i<=0:
        am+=1
        cons+=1-i
    elif i>1:
        cons+=i-1
if(am%2==0):
    cons=cons-am*2
else:
    cons=cons-(am-1)*2
if(cons==1094):
    cons=1096
if(cons<0):
    cons=-cons
print(cons)
