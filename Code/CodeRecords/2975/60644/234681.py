str=input()
for i in range(0,len(str)-1):
    for j in range(0,len(str)):
        if str[j:j+1]<str[j-1:j]:
            temp1=str[j:j+1]
            temp2=str[j-1:j]
            str=str[0:j-1]+temp1+temp2+str[j+1:]
print(str)