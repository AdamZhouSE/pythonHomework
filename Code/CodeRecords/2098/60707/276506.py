a = int(input())
str1 = []
while a > 26:
    tmp = a % 26
    a = int(a / 26)
    if tmp == 0:
        tmp = 26
        a -= 1
    str1.insert(0, chr(tmp + 64))
str1.insert(0, chr(a + 64))
print(''.join(str(i) for i in str1))