string=input()
result=""
temp=''
st=(int)(input())
for i in range(0,len(string)):
    result+=(str)(st+ord(string[i])-ord('A'))
while((result!='100')&(len(result)>2)):
    temp=result
    result=''
    for i in range(1,len(temp)):
        sum=(int)(temp[i])+(int)(temp[i-1])
        if(sum>=10):
            result+=(str)(sum-10)
        else:
            result+=(str)(sum)
print((str)((int)(result)), end="")