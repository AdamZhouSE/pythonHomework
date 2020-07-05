num1=eval(input())
num2=eval(input())
result=[]
for i in range(0,len(num1)):
    for j in range(0,len(num2)):
        if num1[i]==num2[j]:
            result.append(num2[j])
            num2[j]=-1
            break
result.sort()
print(result)