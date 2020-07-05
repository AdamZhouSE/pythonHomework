s=input()
for i in range(5,len(s)):
    if (s[i]==","):
        index=i
        break
for i in range(index,len(s)):
    if(s[i]=='"'):
        index2=i
        break
for i in range(index2+1, len(s)):
    if(s[i]=='"'):
        index3=i
        break
str1=s[5:index-1]
str2=s[index2+1:index3]
str1=sorted(str1)
str2=sorted(str2)
if(str1==str2):
    print("true")
else:
    print("false")