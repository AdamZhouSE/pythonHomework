a = int(input())
s = ''
while a > 0:
    b = a % 26
    a = int(a/26)
    s = chr(ord('a')-1 + b) + s
print(s.upper())