a=str(input())
b=str(input())
len1=len(a)
len2=len(b)
if len1>=len2:
    length=len1
    index=len1-len2
    while index>0:
        b='0'+b
        index=index-1
else:
    length=len2
    index=len2-len1
    while index>0:
        a='0'+a
        index=index-1
result=''
Index=0
for i in range(0,length):
    temp1=a[length-1-i]
    temp2=b[length-1-i]
    if temp1=='0' and temp2=='0' and Index==0:
        result='0'+result
        Index=0
    elif temp1=='0' and temp2=='0' and Index==1:
        result='1'+result
        Index=0
    elif temp1=='1' and temp2=='0' and Index==0:
        result='1'+result
        Index=0
    elif temp1=='0' and temp2=='1' and Index==0:
        result='1'+result
        Index=0
    elif temp1=='1' and temp2=='0' and Index==1:
        result='0'+result
        Index=1
    elif temp1=='0' and temp2=='1' and Index==1:
        result='0'+result
        Index=1
    elif temp1=='1' and temp2=='1' and Index==0:
        result='0'+result
        Index=1
    else:
        result='1'+result
        Index=1
if Index==1:
    result='1'+result
print(result)