num=int(input())
str=input().split(" ")
for i in range(0,len(str)):
    str[i]=int(str[i])
str.sort()
if(len(str)<=2):
    print(0)
else:
    num1=str[1]-str[0]
    num2=str[-1]-str[-2]
    if(num2>num1):
        print(str[-2]-str[0])
    else:
        print(str[-1]-str[1])