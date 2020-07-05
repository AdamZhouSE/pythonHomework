str1=input()
str2=input()
result=0
for i in range(1,len(str1)):
    for j in range(len(str1)-i+1):
      temp=str1[j:j+i]
      result=str2.count(temp)+result
print(result,end="")