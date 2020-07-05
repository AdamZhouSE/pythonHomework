num = input()
isNeg = False
if num[0] == '-':
    isNeg = True
    num = num[1:]
ans = ''
for i in range(0, len(num)):
    ans = num[i]+ans
if isNeg:
    ans = '-'+ans
print(int(ans))

