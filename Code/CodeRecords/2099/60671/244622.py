abc="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
str1=input()
num=int(abc.index(str1[0]))+1
if(len(str1)>1):
    num=num*26+int(abc.index(str1[1]))+1
    
print(num)    
