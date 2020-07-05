s=input()
result=[]
for j in range(1,len(s)):
    if s[j]==s[0]:
        continue
    else:
        if s[j]<s[0]:
            for k in range(j-1):
                result.append(k+1)
            break
        else:break
for i in range(len(s)-1):
    if ord(s[i])<=ord(s[i+1]) :
        if i+1==len(s)-1:
            result.append(i+2)
    else:
        result.append(i+1)
        if i+1==len(s)-1:
            result.append(i+2)
str1=""
for j in range(len(result)):
    str1=str1+str(result[j])+" "

print(str1[0:len(str1)-1])