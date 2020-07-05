list=input()
num1=0
num2=0
count1=0
count2=0
for i in range(len(list)):
    if num1==list[i]:
        count1+=1
    elif num2==list[i]:
        count2+=1
    elif count1==0:
        num1=list[i]
        count1+=1
    elif count2==0:
        num2=list[i]
        count2+=1
    else:
        count1-=1
        count2-=1
count1=0
count2=0
for i in range(len(list)):
    if list[i]==num1:
        count1+=1
    if list[i]==num2:
        count2+=1
res=[]
if count1>int(len(list)/3):
    res.append(num1)
if count2>int(len(list)/3):
    res.append(num2)
print(res)