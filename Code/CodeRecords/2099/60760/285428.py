str0=input()
i=0
length=len(str0)
res=0
while length>0:
    temp=(ord(str0[length-1])-64)*pow(26,i)
    res=res+temp
    i=i+1
    str0=str0[0:length-1]
    length=len(str0)
print(res)