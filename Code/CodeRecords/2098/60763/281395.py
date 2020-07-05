a = int(input())
s = ''
while a > 0:
    b = a % 26
    a = int(a/26)
    if b == 0:
        b = 26
        a-=1
    s = chr(ord('a') - 1 + b) + s
print(s.upper())