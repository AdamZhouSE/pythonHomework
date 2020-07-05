def transToBinary(num):
    temp=""
    while num!=0:
        temp=str(num%2)+temp
        num=num//2
    temp="0"*(32-len(temp))+temp
    return temp

def neg(str):
    i=0
    while i<32:
        if str[i]=='0':
            str=str[0:i]+'1'+str[i+1:]
        else:
            str = str[0:i] + '0' + str[i + 1:]
        i=i+1
    return str

def transToNum(str):
    i=0
    num=0
    while i<32:
        if str[i]=='1':
            num=num+2**(31-i)
        i=i+1
    return num

n=int(input())
i=0
while i<n:
    num=int(input())
    res=transToNum(neg(transToBinary(num)))
    print(res)
    i=i+1