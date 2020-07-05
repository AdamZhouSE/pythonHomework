num=int(input())
num=bin(num)[2:]
result=''
for i in range(len(num)):
    if num[i]=='0':
        result=result+'1'
    else:
        result=result+'0'
result=int(result,2)
print(result)