trueNum = int(input())
answer = ''
if trueNum <= 26:
    print(str(chr(64 + trueNum)), end="")
else:
    while trueNum > 0:
        trueNum -= 1
        a = trueNum // 26
        b = trueNum % 26
        answer += chr(b+65)
        trueNum = a


print(answer[::-1])