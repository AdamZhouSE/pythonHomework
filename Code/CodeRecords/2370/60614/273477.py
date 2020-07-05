num=int(input())
result=''
while num!=1:
    if num%2==0:
        result='0'+result
        num=int(num/-2)
    else:
        num=int(num/-2)+1
        result='1'+result
print('1'+result)