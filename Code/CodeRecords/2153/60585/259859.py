num=input()
isN=0
if num[0]=='-':
    isN=1
    num=num[1:]
while num[-1]=='0':
    num=num[:len(num)-1]
num=num[::-1]
if isN==1:
    num='-'+num
print(num)
