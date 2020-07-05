num1=input()
num2=input()
result=[0 for a in range(len(num1)+len(num2)-1)]
for i in range(len(num1)):
    for j in range(len(num2)):
        result[len(num1)-1-i+len(num2)-1-j]+=int(num1[len(num1)-1-i])*int(num2[len(num2)-1-j])
for i in range(len(result)):
    if result[len(result)-i-1]>9:
        count=0
        while(result[len(result)-i-1]>9):
            result[len(result) - i - 1]=result[len(result)-i-1]-10
            count+=1
        result[len(result) - i - 2]+=count
result_=""
for i in result:
    result_+=str(i)
print(int(result_))
