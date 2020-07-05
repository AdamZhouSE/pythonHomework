str1=str(input())
str2=str(input())
res=0
for i in range(0,len(str1)-len(str2)+1):
    if str1[i:i+len(str2)]==str2:
        res+=1
print(res,end='')