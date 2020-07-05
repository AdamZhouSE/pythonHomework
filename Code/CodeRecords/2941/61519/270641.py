num=int(input())
grade=list(input())
max=0
for i in range(num):
    if grade[i]=="A":
        max=max+4
    if grade[i]=="B":
        max=max+3
    if grade[i]=="C":
        max=max+2
    if grade[i]=="D":
        max=max+1
    if grade[i]=="F":
        max=max+0
if max==0:
    print("0",end="")
else:
    print('%.14f'%(max/num),end="")