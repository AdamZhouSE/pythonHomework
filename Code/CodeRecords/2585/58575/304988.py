str1=list(input())
str2=list(input())

while 'X' in str1:
    str1.remove('X')
while 'X' in str2:
    str2.remove('X')

if str1!=str2:
    print(False)
else:
    print(True)