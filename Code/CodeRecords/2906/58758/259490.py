n = int(input())
message = input()
code = ''
for ch in message:
    ind = (ord(ch)-96+n) % 26
    if ind == 0:
        ind = 26
    code += chr(ind+96)
print(code, end='')
