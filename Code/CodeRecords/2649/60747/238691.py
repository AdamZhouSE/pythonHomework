n=int(input())
string=[]
num=[0for i in range(3)]
sub=0
min1=0
result=[0for i in range(n)]
def binToDec(binary):
    result = 0   #定义一个初始化变量，后续用于存储最终结果
    for i in range(len(binary)):
        #利用for循环及切片从右至左依次取出，然后再用内置方法求2的次方
        result += int(binary[-(i + 1)]) * pow(2, i)
    return result
for i in range(n):
    string.append(input().split(" "))
    for j in range(3):
        num[j]=int(string[i][j])
    num[0]=bin(num[0]).replace('0b','')
    if (num[1]-num[2])>0:
        sub=num[1]-num[2]
        min1=num[2]
    else:
        sub= num[2]-num[1]
        min1=num[1]
    s=[]
    for m in num[0]:
        s.append(m)
    for p in range(len(num[0])-sub-2,len(num[0])-min1+1):
        if s[p]=='0':
            s[p]='1'
        else:s[p]='0'
    result[i]=binToDec(''.join(s))
for i in range(n):
    print(result[i])
