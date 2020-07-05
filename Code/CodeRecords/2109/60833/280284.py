str1=str(input())
while(len(str1)>1):
    res=0
    for i in range(0,len(str1)):
        res+=int(str1[i])
    str1=str(res)    
print(str1)