str=input()
str=str[1:len(str)-1]
str=str.split(",")

for i in range (0,len(str)):
    str[i]=int(str[i])
for i in range (1,len(str)):
    if((str[i]>str[i-1]) & (str[i]>str[i+1])):
        print(i)
        break;
