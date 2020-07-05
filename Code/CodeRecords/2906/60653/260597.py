n = int(input()) % 26
s = list(input())
ans = []
for i in s:
    a = n + ord(i) - ord('0')
    if a > ord('z') - ord('0'):
        a -= 26
    ans.append(chr(a+ord('0')))
print("".join(str(n) for n in ans), end='')