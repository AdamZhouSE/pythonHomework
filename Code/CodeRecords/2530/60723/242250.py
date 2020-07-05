str1=input()
str2=input()
array=list(str2)
result=""
for i in range(len(str1)):
    result=result+str1[i]*array.count(str1[i])
    array.remove(str1[i])
result=result+''.join(array)
print(result)