str=input()
len=str.__len__()
i=len-1
while i>-1:
    str=str+str[i]
    i=i-1
print(str)