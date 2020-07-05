l1=eval(input())
l2=eval(input())
l1=list(reversed(l1))
l2=list(reversed(l2))
length=max(len(l1),len(l2))
result=0
for i in range(length):
    temp=int(pow(-2,i))
    if i<len(l1):
        result=result+l1[i]*temp
    if i<len(l2):
        result+=l2[i]*temp
print(result)
    
