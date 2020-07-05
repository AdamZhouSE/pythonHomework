ranges=eval(input())
result=(int)(ranges[0])
for i in range((int)(ranges[0])+1,(int)(ranges[1])+1):
    result=result&i
print(result)