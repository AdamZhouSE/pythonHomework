def cut(str1,str2,l):
    list=[]
    result=0
    for k in range(1,l+1):
        for i in range(0,len(str1)-k+1):
            a1=str1[i:i+k]
            for j in range(0,len(str2)-k+1):
                a2=str2[j:j+k]
                if a1==a2:
                    result=result+1
    return result
str1=input()
str2=input()
l=0
if(len(str1)<len(str2)):
    l=len(str1)
else:
    l=len(str2)
print(cut(str1,str2,l),end="")