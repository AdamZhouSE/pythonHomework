arr=eval(input())
num1=None
num2=None
count1=0
count2=0
result=[]
for i in arr:
    if num1==i:
        count1+=1
    elif num2==i:
        count2+=1
    elif count1==0:
        num1=i
        count1=1
    elif count2==0:
        num2=i
        count2=1
    else:
        count1-=1
        count2-=1
count1=count2=0
for i in arr:
    if i==num1:count1+=1
    elif i==num2:count2+=1
if count1>(len(arr)//3):
    result.append(num1)
if count2>(len(arr)//3):
    result.append(num2)
print(result)