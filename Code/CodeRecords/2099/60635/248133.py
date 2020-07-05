src = input()
num = [ord(x)-ord('A')+1 for x in src]
num = num[::-1]
step = 1
ans = 0
for n in num:
    ans += n*step
    step *= 26
print(ans)