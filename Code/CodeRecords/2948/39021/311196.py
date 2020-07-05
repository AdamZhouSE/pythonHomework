def calcu(s):
    next=''
    for i in range(len(s)-1):
        num = int(s[i])+int(s[i+1])
        next += str(num%10)
    return next


s= input()
st = int(input())
str1 = ''
for i in range(len(s)):
    num = ord(s[i])-ord('A') + st
    str1 += str(num)
flag = 1
res = calcu(str1)
while(flag):
    res = calcu(res)
    if int(res)<=100:
        flag = 0
    else:
        flag = 1

print(int(res),end='')




    