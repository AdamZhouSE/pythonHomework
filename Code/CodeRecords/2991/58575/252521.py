str=input()
len=str.__len__()
i=len-1
temp=""
while i>=0:
    temp=temp+str[i]
    i=i-1
print(temp,end="")