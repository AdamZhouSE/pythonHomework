length=int(input())
str=input()
result=0
for i in range(length):
    if(str[i]=="V"):
        temp=str[0:i]+("K")+(str[i+1:length])
    else:
        temp = str[0:i] + ("V") + (str[i+1:length])
    if temp.count("VK")>=result:
        result=temp.count("VK")
print(result)