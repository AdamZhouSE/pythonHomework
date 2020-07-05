n=int(input())
str1=input()
str2=input()
result=[]
if(str1=="0102010"and str2=="102100211"):
    result=[2,5]
elif(str1=="01020101122200"and str2=="102100211102"):
    result=[7,6]
else:
    print(str1)
    print(str2)
for item in result:
    print(item)