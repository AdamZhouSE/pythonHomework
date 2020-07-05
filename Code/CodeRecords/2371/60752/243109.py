import re


num=int(input())
for i in range (num):
    string=input().lower()
    a=''.join(re.findall(r'[a-z]',string))
    b=list(a)
    b.reverse()
    b=''.join(b)
    if a==b:
        print('YES')
    else:
        print('NO')


