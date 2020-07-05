src1=input()
src2=input()


def btod(src):
    step = 1
    ans = 0
    for n in src:
        ans += int(n)*step
        step *= 2
    return ans


num1=btod(list(src1)[::-1])
num2=btod(list(src2)[::-1])
print(bin(num1+num2)[2:])