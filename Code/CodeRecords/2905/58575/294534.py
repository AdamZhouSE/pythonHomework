def transToNum(str):
    i=0
    num=0
    while i<len(str):
        if str[i]=='1':
            num=num+2**(len(str)-i-1)
        i=i+1
    return num

str=list(input()[1:-1].split(","))
str=''.join(str)
res=transToNum(str)
print(res)