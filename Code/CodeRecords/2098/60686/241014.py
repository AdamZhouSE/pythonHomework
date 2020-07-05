n = int(input())
res = []


def convert(num):
    if num > 26:
        res.append(chr(64 + num % 26))
        convert(int(num / 26))
    else:
        res.append(chr(64 + num))
    return


convert(n)
print("".join(res)[::-1])
