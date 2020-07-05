s=input()
s=s.lstrip()
start=s[0]
result=''
sign=''
if start=='+' or start=='-':
    sign=start
    s=s[1:]
    start=s[0]
if start>='0' and start<='9':
    for item in s:
        if item>='0' and item<='9':
            result=result+item
        else:
            break
else:
    result='0'
num=int(result)
if sign=='-':
    num=-num
if num<-2147483648:
    num=-2147483648
print(num)