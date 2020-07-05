str1=input()
str2=input()
result=0
for i in range(1,len(str1)+1):
    for j in range(len(str1)-i+1):
      temp=str1[j:j+i]
      for n in range(len(str2)-len(temp)+1):
                 if str2[n:n+len(temp)]==temp:
                     result=result+1
print(result,end="")