def calcu(s):
    next=''
    for i in range(len(s)-1):
        num = int(s[i])+int(s[i+1])
        next = str(num%10)+next
    return next


s= input()
st = int(input())
print(st)
str1 = ''
for i in range(len(s)):
    num = ord(s[i])-ord('a') +st
    str1 = str(num)+str1
flag = 1
print(str1)
res = calcu(str1)
while(flag):
    res = calcu(res)
    if len(res)<3 or res =='100':
        flag = 0
    else:
        flag = 1
    print(res)

print(res)




    