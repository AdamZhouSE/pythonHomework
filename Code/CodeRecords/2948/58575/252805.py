str1=input()
ST=input()
ST=int(ST)
len_Name=str1.__len__()
i=0

res=""
while i<len_Name:
    res=res+str(ord(str1[i])-ord('A')+ST)
    i=i+1

temp=res
res=list(res)
j=int(temp)
while j>100:
    len=res.__len__()
    i=0

    while i<len-1:
        res[i]=str(int(temp[i])+int(temp[i+1]))[-1]
        i=i+1
    del res[-1]
    temp=''.join(res)

    j=int(temp)
print(j,end="")