import re
num=re.split('\D',input())
num2=[]

for i in range(num.__len__()):
    if i%4==2:
        num[i]=str(int(num[i])+1)
        num[i+1]=str(int(num[i+1])+1)
        num2.append(num[i]+num[i+1])
num=num2
A=[]
B=[]
for i in range(num.__len__()):
    if i%2==0:
        A.append(num[i])
    else:
        B.append(num[i])
W1={"11","22","33"}
W2={"13","22","31"}
W3={"11","21","31"}
W4={"12","22","3"}
W5={"13","23","33"}
W6={"11","12","13"}
W7={"21","22","23"}
W8={"31","32","33"}
Wlist=[W1,W2,W3,W4,W5,W6,W7,W8]
Winner="Pending"
for i in Wlist:
    if i.issubset(A):
        Winner="A"
        break
    if i.issubset(B):
        Winner="B"
        break
if Winner!="A" or Winner!="B":
    if num.__len__()==9:
        Winner="Draw"
print(Winner)