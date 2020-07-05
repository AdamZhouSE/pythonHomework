n=int(input())
list1=list(input())
sum=0
for i in list1:
    if i=="A":
        sum+=4
    elif i=="B":
        sum+=3
    elif i=="C":
        sum+=2
    elif i=="D":
        sum+=1  
if sum==0:
    print("0",end="")
else:
    print('%.14f' % (sum/n),end="") 