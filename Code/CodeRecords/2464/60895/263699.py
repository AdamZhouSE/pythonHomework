num=int(input())
s=input().split(',')
length=1
result=0
while length<=len(s):
    for i in range(0,len(s)+1-length):
        temp=length
        sum=0
        while temp>=1:
            sum=sum+int(s[i+temp-1])
            temp=temp-1
        if sum>=num:
            result=length
            break
    if result!=0:
        break
    else:
        length=length+1
print(result)
                        